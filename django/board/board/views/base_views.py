from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from board.models import Question, QuestionCount
from board.forms import QuestionForm, AnswerForm, CommentForm


from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from django.utils import timezone

from django.contrib import messages

from django.db.models import Q, Count  #  Q:or 조건으로 데이터 조회

from tools.utils import get_client_ip

#  Count:카운터 가능


def question_list(request):
    """전체 질문 추출"""

    # 현재 페이지 번호 가져오기
    page = request.GET.get("page", 1)
    # 검색어 가져오기
    keyword = request.GET.get("keyword", "")
    # 정렬기준 가져오기
    so = request.GET.get("so", "recent")

    # question_list = Question.objects.all()
    # question_list = Question.objects.order_by("-created_at")

    if so == "recommend":
        # question_list 테이블에 annotate 함수로 "num_voter" 이름으로 카운트세서 임시필드명 생성 해줘 그래야 정렬이 쉬움
        question_list = Question.objects.annotate(num_voter=Count("voter")).order_by(
            "-num_voter", "created_at"
        )
    elif so == "popular":
        question_list = Question.objects.annotate(num_answer=Count("answer")).order_by(
            "-num_answer", "created_at"
        )
    else:
        question_list = Question.objects.order_by("-created_at")

    if keyword:
        question_list = Question.objects.filter(
            Q(subject__icontains=keyword)
            | Q(content__icontains=keyword)
            | Q(author__username__icontains=keyword)
            | Q(answer__author__username__icontains=keyword)
        ).distinct()  # distinct() : 중복은 제거 하고 추출

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {"question_list": page_obj, "page": page, "keyword": keyword, "so": so}
    return render(request, "board/question_list.html", context)


def question_detail(request, qid):
    question = get_object_or_404(Question, id=qid)

    # 클라이언트 ip 가져오기

    ip = get_client_ip(request)
    cnt = QuestionCount.objects.filter(ip=ip, question=question).count()

    if cnt == 0:

        # QuestionCount 객체 생성 후 저장
        qc = QuestionCount(ip=ip, question=question)

        qc.save()

        # QuestionCount 객체에 view_cnt +1 추가 후 저장
        if question.view_cnt:
            question.view_cnt += 1
        else:
            question.view_cnt = 1
        question.save()

    # 현재 페이지 번호 가져오기
    page = request.GET.get("page", 1)
    # 검색어 가져오기
    keyword = request.GET.get("keyword", "")
    # 정렬기준 가져오기
    so = request.GET.get("so", "recent")

    #
    context = {"question": question, "page": page, "keyword": keyword, "so": so}
    return render(request, "board/question_detail.html", context)
