from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo

from .forms import PhotoForm


def edit(request, id):
    photo = get_object_or_404(Photo, id=id)
    if request.method == "POST":
        # 사용자의 입력값을 가지고올떄는 request.POST 한다
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect("photo_detail", id=id)
    else:
        # 내가 찾은걸 연결 시켜야 하기에 instance=photo 이런식으로 연결한다
        # 이게 create 랑 다른 점이다
        form = PhotoForm(instance=photo)
    return render(request, "photo/photo_edit.html", {"form": form})


def remove(request, id):
    photo = get_object_or_404(Photo, id=id)
    photo.delete()

    return redirect("photo_list")


def detail(request, id):

    photo = get_object_or_404(Photo, id=id)  # 앞쪽은 모델명 뒤에는 뭐가지고 와야 하는지

    return render(request, "photo/photo_detail.html", {"photo": photo})


def list(request):
    photos = Photo.objects.all()

    return render(request, "photo/photo_list.html", {"photos": photos})


def create(request):

    if request.method == "POST":
        form = PhotoForm(request.POST)
        if form.is_valid():  # 유효성(모델 정의된 규칙)
            form.save()  # model.save() 호출됨

            return redirect("photo_list")
    else:
        form = PhotoForm()

    form = PhotoForm()

    return render(request, "photo/photo_create.html", {"form": form})
