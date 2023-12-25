from django.contrib import admin

from comment.models import Post, Comment, PostMedia


class PostMediaInline(admin.TabularInline):
    model = PostMedia


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'updated', 'avg_rating', 'like_post_count', 'comment_count')
    search_fields = ('slug', 'body')
    list_filter = ('updated',)
    prepopulated_fields = {'slug': ('body',)}
    raw_id_fields = ('user',)
    inlines = [PostMediaInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'created', 'is_reply', 'like_comment_count')
    raw_id_fields = ('user', 'post', 'reply')
