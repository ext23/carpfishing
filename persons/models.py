from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


class Person(models.Model):

    last_name = models.CharField(max_length=100, help_text='Фамилия')
    first_name = models.CharField(max_length=100, help_text='Имя')
    patronymic = models.CharField(max_length=100, help_text='Отчество', blank=True)
    photo = models.ImageField(help_text='Фотография', blank=True)
    user = models.OneToOneField(User, related_name='member', on_delete=models.CASCADE, help_text='Пользователь')
    phone = models.CharField(max_length=11, help_text='Номер телефона', blank=True)
    pin = models.CharField(max_length=4, help_text='Пин-код', blank=True)
    is_test = models.BooleanField(default=False, help_text='Тестовый участник')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    def image_tag(self):
        return mark_safe('<img src="{}" height="20"/>'.format(self.photo.url))

    image_tag.short_description = 'Image'
