from django.forms.utils import ErrorList


class MyErrorList(ErrorList):
    def as_text(self):
        return '\n'.join(self)
