from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_filter = ('category', 'tag', 'created_at' )
    list_display = ('title', 'id', 'category', 'created_at', 'updated_at')
    search_fields = ('title', )
    filter_horizontal = ('tag',)
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    list_filter = ('name', 'created_at',)
    search_fields = ('name', 'email', 'message')


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Article, ArticleAdmin)
