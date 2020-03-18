from django.contrib import admin
from .models import Activity, Interest


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
