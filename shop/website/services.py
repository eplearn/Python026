from .models import NoteModel
from .forms import NoteForm


def get_all_notes():
    notes = NoteModel.objects.all()
    context = {
        'notes': notes
    }
    return context


# def create_note(request):
#     error = ''
#     if request.method == 'POST':
#         form = NoteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             context = {
#                 'form': form,
#                 'error': error
#             }
#             return context
#         else:
#             error = 'wrong input data'
#             context = {
#                 'error': error
#             }
#             # print('error')
#             return context

def create_note(request):
    error = ''
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'form': form,
                'error': error,
            }
            return context
        else:
            error = 'wrong input data'
            context = {
                'error': error,
            }
            # print('error')
            return context
