from django.db import models


# Create your models here.
class Account(models.Model):
    login = models.CharField('login', max_length=30)
    email = models.EmailField('email', max_length=254)
    password = models.CharField('password', max_length=30)
    nickname = models.CharField('nickname', max_length=30)

    def __str__(self):
        return self.nickname
