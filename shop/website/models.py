from datetime import datetime

from django.core.validators import MinLengthValidator
from django.urls import reverse
from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class NoteModel(models.Model):
    author = models.CharField('author', max_length=30, validators=[MinLengthValidator(5, 'Minimum 5 characters required')])
    title = models.CharField('title', max_length=30)
    category = models.CharField('category', max_length=30)
    abstract = models.CharField('abstract', max_length=300)
    text = models.TextField('text', validators=[MinLengthValidator(25, 'Note main text should contain a minimum of 25 characters')])
    publish_date = models.DateTimeField('publish date', default=datetime.now())
    is_published = models.BooleanField('is published?', default=True)

    def get_absolute_url(self):
        return reverse('website:create_note', kwargs={'id': self.pk})

    def __str__(self):
        return str(self.title) + ' - ' + str(self.publish_date)

    # def clean(self):
    #     if len(str(self.author)) < 5:
    #         # raise ValidationError(
    #         #     {'author': 'Minimum 5 characters required'},
    #         # )
    #         self.add_error('author', 'Minimum 5 characters required')
    #     if len(str(self.text)) < 25:
    #         # raise ValidationError(
    #         #     {'text', 'Note main text should contain a minimum of 25 characters'},
    #         # )
    #
    # def save(self, *args, **kwargs):
    #     self.full_clean()
    #     return super().save(*args, **kwargs)
