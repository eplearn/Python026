from django.urls import path
from . import views
from .views import CreateNote, NotesView, DltNote, ShowNote

app_name = 'website'
urlpatterns = [
    path('', NotesView.as_view(), name='index'),
    path('create_note', CreateNote.as_view(), name='create-note'),
    path('note/<int:pk>/delete/', DltNote.as_view(), name='delete-note'),
    path('note/<int:pk>', ShowNote.as_view(), name='show-note')
]
