from django.forms.utils import ErrorList


# class MyErrorList(ErrorList):
#     def as_text(self):
#         return '\n'.join(self)

class DataMixin:
    def get_user_context(self, **kwargs) -> dict:
        context = kwargs

        if self.request.user.is_authenticated():
            context['is_authenticated'] = True
        else:
            context['is_authenticated'] = False

        return context
