from django.urls import path
from .views import CreateNote, NotesView, DltNote, ShowNote, RegisterUser, LoginUser, logout_user, UserProfile

app_name = 'website'
urlpatterns = [
    path('', NotesView.as_view(), name='index'),
    path('create_note', CreateNote.as_view(), name='create-note'),
    path('note/<int:pk>/delete/', DltNote.as_view(), name='delete-note'),
    path('note/<int:pk>', ShowNote.as_view(), name='show-note'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('user_profile',  UserProfile.as_view(), name='user-profile'),
]
