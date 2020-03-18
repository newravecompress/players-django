from django.contrib import admin
from .models import Community, Member


@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active', 'type', 'date_create', 'date_update')
    list_display_links = ('name', 'code')
    search_fields = ('name',)
    list_filter = ('name', 'code', 'is_active', 'type')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'community', 'date_create', 'date_update')
    list_display_links = ('user', 'community')
    search_fields = ('user', 'community')
    list_filter = ('user', 'community')
