from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo


# Create your views here.


def list(request):
    """
    html 응답
    """
    # todos = Todo.objects.all() # 전부부르기

    # 이렇게하면 컴플리디트가 펄스인 것만 가져온다
    todos = Todo.objects.filter(completed=False)
    # 이렇게 하면  html 응답
    return render(request, "todo/todo_list.html", {"todos": todos})


def done_list(request):

    dones = Todo.objects.filter(completed=True)

    return render(request, "todo/done_list.html", {"dones": dones})


def create(request):
    """

    get/post 둘다처리

    """

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        important = request.POST.get("important")

        print("전송내용", title, description, important)

        if important:
            todo = Todo(title=title, description=description, important=True)
        else:
            todo = Todo(title=title, description=description)
        todo.save()
        return redirect("list")

    return render(request, "todo/todo_create.html")


def read(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, "todo/todo_detail.html", {"todo": todo})


def done(request, id):
    # 수정할  model 찾기
    todo = Todo.objects.get(id=id)
    # 변경 내용 삽입
    todo.completed = True
    # 저장
    todo.save()
    # 다하면 리스트로
    return redirect("list")


def edit(request, id):

    todo = Todo.objects.get(id=id)
    if request.method == "POST":
        important = request.POST.get("important")
        description = request.POST.get("description")

        todo.description = description
        if important:
            todo.important = True
        else:
            todo.important = False
        todo.save()
        return redirect("read", id=id)

    return render(request, "todo/todo_edit.html", {"todo": todo})


# def list(request):
#     """
#     일반 문자열 응답
#     """
#     return HttpResponse("Hello")
