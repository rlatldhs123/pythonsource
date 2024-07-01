from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


from django.core.paginator import Paginator


def delete(requst, post_id):

    post = get_object_or_404(Post, id=post_id)
    post.delete()

    return redirect("blog:list")


def modify(requst, post_id):

    post = get_object_or_404(Post, id=post_id)
    if requst.method == "POST":
        form = PostForm(requst.POST, requst.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = requst.user
            post.save()

            return redirect("blog:detail", post.id)

    else:
        form = PostForm(instance=post)

    return render(requst, "blog/modify.html", {"form": form, "post": post})


@login_required(login_url="common:login")
def create(requst):

    if requst.method == "POST":

        # 폼에 post 로 넘어오는 내용 담기

        form = PostForm(requst.POST, requst.FILES)

        # 폼 유효성 검증
        if form.is_valid():

            # 유효성 통과 하면 저장
            post = form.save(commit=False)
            post.user = requst.user
            post.save()

        # 리스트로 이동
        return redirect("blog:list")
        # return redirect("blog:detail", post.id)

    else:
        form = PostForm()

    return render(requst, "blog/create.html", {"form": form})


def list(requst):

    page = requst.GET.get("page", 1)

    posts = Post.objects.all()
    # 한페이지에 보여주는 게시물 수
    paginator = Paginator(posts, 5)
    page_obj = paginator.get_page(page)

    context = {"posts": page_obj}

    return render(requst, "blog/list.html", context)


def detail(requst, post_id):

    post = get_object_or_404(Post, id=post_id)

    context = {"post": post}
    return render(requst, "blog/post.html", context)
