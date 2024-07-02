from django.contrib import admin

from .models import Post
from .models import Comment


# admin.site.register(Post)
# admin.site.register(Comment)


# Register your models here.

## 해당 코드로 어드민을 꾸밀 수있다


class PostAdmin(admin.ModelAdmin):

    # 어드민 사이트에서 보여줄 컬럼 정하기
    list_display = ("title", "created_at", "user")
    # 링크해서 들어갈 컬럼 정하기
    list_display_links = ["title"]
    # 기준으로 검색할 창을 만든다
    search_fields = ["title"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at")


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
