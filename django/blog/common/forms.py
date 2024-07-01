from django import forms

from django.contrib.auth.forms import UserCreationForm

from blog.models import Post
from django.contrib.auth.models import User


user = User.objects.get(id=1)

for i in range(100):
    p = Post(title="테스트데이터:[%03d]" % i, content="내용 없음", user=user)
    p.save()


class UserForm(UserCreationForm):

    email = forms.EmailField(label="이메일", help_text="사용할 이메일을 입력해 주세요")

    class Meta:
        model = User
        fields = ["username", "email"]
        labels = {"username": "아이디"}
