from django.contrib import admin
from .models import NoteModel


class NoteAdmin(admin.ModelAdmin):
    search_fields = ('title', 'category', 'abstract', 'text')
    list_display = ('id', 'is_published', 'author', 'title', 'category', 'publish_date', 'abstract', 'text')
    list_display_links = ('id', 'title',)
    list_editable = ('author', 'category', 'is_published', 'abstract', 'text')


# Register your models here.
admin.site.register(NoteModel, NoteAdmin)
