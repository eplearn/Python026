from django.shortcuts import render
from django.views.generic import CreateView

from . import services
from .forms import NoteForm
from .models import NoteModel


# Create your views here.
def index(request):
    return render(request, 'website/index.html', services.get_all_notes())


class CreateNote(CreateView):
    form_class = NoteForm
    template_name = 'website/create_note.html'
    success_url = '/create_note'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = NoteModel.objects.all()
        return context
