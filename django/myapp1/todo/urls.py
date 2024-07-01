from django.urls import path
from . import views


urlpatterns = [
    # /todo/
    path("", views.list, name="list"),
    # /todo/create
    path("create/", views.create, name="create"),
    # /<int>,<string> 등 어떤 데이터타입의 pk 가 넘어올 것인지 적어준다
    # /todo/2
    path("<int:id>/", views.read, name="read"),
    # /todo/edit/2
    path("edit/<int:id>/", views.edit, name="edit"),
    # /todo//done/2
    path("done/<int:id>/", views.done, name="done"),
    # /todo/done
    path("done/", views.done_list, name="done_list"),
]
