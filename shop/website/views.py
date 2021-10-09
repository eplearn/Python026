from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import services
from .forms import NoteForm, RegisterUserForm, LoginUserForm
from .models import NoteModel
from .utils import DataMixin


# Create your views here.
# def index(request):
#     return render(request, 'website/index.html', services.get_all_notes())

class NotesView(ListView):
    model = NoteModel
    template_name = 'website/index.html'
    context_object_name = 'notes'

    # extra_context = {'title': 'Main'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main'
        return context

    def get_queryset(self):
        return NoteModel.objects.filter(is_published=True)


class CreateNote(LoginRequiredMixin, DataMixin, CreateView):
    form_class = NoteForm
    template_name = 'website/create_note.html'
    # success_url = '/create_note'
    success_message = 'Note successfully created!'
    error_message = 'Error saving the Note, check fields below.'
    login_url = reverse_lazy('website:index')
    success_url = reverse_lazy('website:create-note')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = NoteModel.objects.all()
        return context


class DltNote(DeleteView):
    model = NoteModel
    success_url = '/create_note'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ShowNote(DetailView):
    model = NoteModel
    template_name = 'website/show_note.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'note'


class RegisterUser(DataMixin, CreateView):
    # form_class = UserCreationForm
    form_class = RegisterUserForm
    template_name = 'website/register.html'
    success_url = reverse_lazy('website:index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= self.get_user_context(title='Registration')
        return context


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'website/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= self.get_user_context(title='Enter')
        return context

    def get_success_url(self):
        return reverse_lazy('website:index')


def logout_user(request):
    logout(request)
    return redirect('website:index')


class UserProfile:
    pass
