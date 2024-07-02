from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from .models import Post, Comment
from .forms import PostForm
from django.contrib.auth.decorators import login_required


from django.core.paginator import Paginator
from django.http import JsonResponse


def comment_create(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        content = request.POST.get("content").strip()
        comment = Comment.objects.create(user=request.user, post=post, content=content)
        return redirect("blog:detail", post_id=post.id)

    return redirect("blog:detail", post_id)


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

            # 태그 저장하는 코드
            #  form.save_m2m() <<<

            form.save_m2m()

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

    # 로그인 유저가 해당 게시물에 좋아요를 했는지 안했는지
    is_liked = False

    if post.likes.filter(id=requst.user.id).exists():
        is_liked = True

    return render(requst, "blog/post.html", {"post": post, "is_liked": is_liked})


def post_like(requst, post_id):
    post = get_object_or_404(Post, id=post_id)
    # 로그인 유저가 해당 게시물에 좋아요 했는지 여부
    is_liked = post.likes.filter(id=requst.user.id).exists()

    is_liked_change = False
    if is_liked:
        post.likes.remove(requst.user)
    else:
        post.likes.add(requst.user)
        is_liked_change = True

    return JsonResponse({"likes": post.likes.count(), "is_liked": is_liked_change})
