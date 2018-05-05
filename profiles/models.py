from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    login_name = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15, verbose_name='Имя')
    last_name = models.CharField(max_length=15, verbose_name='Фамилия')
    photo = models.ImageField(upload_to='profiles/{0}/photo'.format(User.username), verbose_name='Фото')


