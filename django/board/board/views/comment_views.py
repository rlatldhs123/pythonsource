from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from board.models import Question, Answer, Comment
from board.forms import QuestionForm, AnswerForm, CommentForm

from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from django.utils import timezone

from django.contrib import messages

from django.db.models import Q, Count  #  Q:or 조건으로 데이터 조회

#  Count:카운터 가능


@login_required(login_url="common:login")
def comment_create_question(request, qid):
    question = get_object_or_404(Question, id=qid)
    if request.method == "POST":
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.author = request.user
        comment.question = question
        comment.save()
        # return redirect("board:question_detail", qid)
        return redirect(
            "{}#comment_{}".format(
                resolve_url("board:question_detail", qid=qid),
                comment.id,
            )
        )

    else:
        form = CommentForm()
    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="common:login")
def comment_modify_question(request, cid):
    comment = get_object_or_404(Comment, id=cid)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        comment = form.save(commit=False)
        comment.modified_at = timezone.now()
        comment.save()
        # return redirect("board:question_detail", comment.question.id)
        return redirect(
            "{}#comment_{}".format(
                resolve_url("board:question_detail", qid=comment.question.id),
                comment.id,
            )
        )

    else:
        form = CommentForm(instance=comment)
    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="common:login")
def comment_delete_question(request, cid):
    comment = get_object_or_404(Comment, id=cid)
    comment.delete()
    return redirect("board:question_detail", comment.question.id)


@login_required(login_url="common:login")
def comment_create_answer(request, aid):
    answer = get_object_or_404(Answer, id=aid)
    if request.method == "POST":
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.author = request.user
        comment.answer = answer
        comment.save()
        # return redirect("board:question_detail", answer.question.id)
        return redirect(
            "{}#comment_{}".format(
                resolve_url("board:question_detail", qid=answer.question.id),
                comment.id,
            )
        )
    else:
        form = CommentForm()
    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="common:login")
def comment_modify_answer(request, cid):
    comment = get_object_or_404(Comment, id=cid)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        comment = form.save(commit=False)
        comment.modified_at = timezone.now()
        comment.save()
        # return redirect("board:question_detail", comment.answer.question.id)
        return redirect(
            "{}#comment_{}".format(
                resolve_url("board:question_detail", qid=comment.answer.question.id),
                comment.id,
            )
        )

    else:
        form = CommentForm(instance=comment)
    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="common:login")
def comment_delete_answer(request, cid):
    comment = get_object_or_404(Comment, id=cid)
    comment.delete()
    return redirect("board:question_detail", comment.answer.question.id)
