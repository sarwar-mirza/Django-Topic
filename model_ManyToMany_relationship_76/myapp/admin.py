from django.contrib import admin
from myapp.models import Song
# Register your models here.
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_name', 'song_duration', 'writer_by']
