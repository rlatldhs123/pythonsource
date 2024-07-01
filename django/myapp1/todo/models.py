from django.db import models

# 테이블과 동일한 모델 정의


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    # auto_now_add : 새글등록시 자동으로 날짜 추가됨
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    # 자바의 toString 과 같은 역할
    def __str__(self) -> str:
        return self.title
