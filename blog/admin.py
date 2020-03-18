from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'author', 'status', 'date_create', 'date_update')
    list_display_links = ('title', 'code')
    search_fields = ('title', )
    list_filter = ('title', 'author', 'status', 'date_create', 'date_update')