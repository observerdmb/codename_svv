from django.contrib.auth.models import User
from django.db import models
from PIL import Image

def upload_to(instance, filename):
    return 'images/%s/%s' % (instance.user.user.username, filename)

class Person(models.Model):
    login_name = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    nick_name = models.CharField(max_length=20, verbose_name='Псевдоним', blank=True)
    country = models.CharField(max_length=20, verbose_name='Страна', blank=True)
    city = models.CharField(max_length=20, verbose_name='Город', blank=True)
    about_me = models.TextField(verbose_name='Обо мне', default=None, blank=True, null=True)
    photo = models.ImageField(upload_to='profiles//%Y/%m/%d/', verbose_name='Фото', blank=True, null=True)

    def __str__(self):
        if self.last_name:
            return str(self.last_name) + ' ' + str(self.first_name)
        else:
            return self.first_name

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def save(self, *args, **kwargs):
        super(Person, self).save(*args, **kwargs)
        if self.photo:
            wanted_dim = 250
            file = self.photo.path
            height = self.photo.height
            width = self.photo.width
            if width != wanted_dim:
                max_side = max(height, width)
                k = wanted_dim / max_side
                new_width = round(width * k)
                new_height = round(height * k)
                picture = Image.open(file)
                picture = picture.resize((new_width, new_height), Image.ANTIALIAS)
                picture.save(file)