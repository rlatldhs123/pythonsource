from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/photo/
    path("", views.list, name="photo_list"),
    #
    path("new/", views.create, name="photo_create"),
    #
    path("<int:id>/", views.detail, name="photo_detail"),
    #
    path("remove/<int:id>/", views.remove, name="photo_remove"),
    #
    path("edit/<int:id>/", views.edit, name="photo_edit"),
]
