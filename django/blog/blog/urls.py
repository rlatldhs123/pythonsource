from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.list, name="list"),
    # /blog/post/2  게시물 상세 보기
    path("post/<int:post_id>/", views.detail, name="detail"),
    # /blog/post/create
    path("post/create/", views.create, name="create"),
    # /blog/post/modify/1
    path("post/modify/<int:post_id>", views.modify, name="modify"),
    # /blog/post/delete/1
    path("post/delete/<int:post_id>", views.delete, name="delete"),
]
