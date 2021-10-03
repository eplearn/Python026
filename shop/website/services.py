from .models import NoteModel


def get_all_notes():
    notes = NoteModel.objects.all()
    context = {
        'notes': notes
    }
    return context
