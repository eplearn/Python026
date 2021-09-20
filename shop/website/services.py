from .models import Account
from .forms import AccountForm


def get_all_accounts():
    accounts = Account.objects.all()
    context = {
        'accounts': accounts
    }
    return context


def create_account(request):
    error = ''
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'form': form,
                'error': error
            }
            return context
        else:
            error = 'wrong input data'
            context = {
                'error': error
            }
            return context
