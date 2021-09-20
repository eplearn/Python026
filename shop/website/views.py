from django.shortcuts import render
from . import services
from .forms import AccountForm


# Create your views here.
def index(request):
    return render(request, 'website/index.html', services.get_all_accounts())


def create_account(request):
    services.create_account(request)
    form = AccountForm()
    error = ''
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'website/create_account.html', context)
