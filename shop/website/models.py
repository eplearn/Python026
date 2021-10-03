from datetime import datetime
from django.db import models


# Create your models here.
class NoteModel(models.Model):
    author = models.CharField('author', max_length=30)
    title = models.CharField('title', max_length=30)
    category = models.CharField('category', max_length=30)
    abstract = models.CharField('abstract', max_length=300)
    text = models.TextField('text')
    publish_date = models.DateTimeField('publish date', default=datetime.now())

    def __str__(self):
        return str(self.title) + ' - ' + str(self.publish_date)
