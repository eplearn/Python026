from django.urls import path
from . import views
from .views import CreateNote

app_name = 'website'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_note', CreateNote.as_view(), name='create-note'),
]
