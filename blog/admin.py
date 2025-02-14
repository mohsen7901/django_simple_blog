from django.contrib import admin
from blog.models import Post, Category, Tag, Comment
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-'
    # fields = ['title', 'content', 'post_status', ]
    list_display = ('id', 'title', 'author', 'post_status', 'updated_date', 'published_date')
    list_filter = ['title', 'post_status', 'categories', 'tags']
    search_fields = ['title', 'content']
    list_display_links = ['id', 'title']
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-'
    list_display = ['name', 'email', 'text', 'is_approved', 'post']
    list_filter = ['name', 'is_approved','post']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)