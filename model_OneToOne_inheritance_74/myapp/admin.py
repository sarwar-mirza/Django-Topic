from django.contrib import admin
from myapp.models import Page, Like
from django.dispatch import receiver

# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['page_name', 'page_cat', 'page_publish_date', 'user']

@admin.register(Like)
class PageAdmin(admin.ModelAdmin):
    list_display = ['page_name', 'page_cat', 'page_publish_date', 'user', 'likes', 'user_inherit']
