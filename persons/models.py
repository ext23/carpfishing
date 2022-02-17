from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


class Person(models.Model):
    last_name = models.CharField(max_length=100, help_text='Фамилия')
    first_name = models.CharField(max_length=100, help_text='Имя')
    patronymic = models.CharField(max_length=100, help_text='Отчество', blank=True)
    photo = models.ImageField(help_text='Фотография', blank=True)
    user = models.OneToOneField(User, related_name='member', on_delete=models.CASCADE, help_text='Пользователь', blank=True, null=True)
    phone = models.CharField(max_length=11, help_text='Номер телефона', blank=True)
    pin = models.CharField(max_length=4, help_text='Пин-код', blank=True)
    is_test = models.BooleanField(default=False, help_text='Тестовый участник')

    def __str__(self):
        return f'{self.last_name} {self.first_name} ({self.user})'

    def image_tag(self):
        return mark_safe('<img src="{}" height="20"/>'.format(self.photo.url))

    image_tag.short_description = 'Image'


class Member(models.Model):
    person = models.OneToOneField(Person,
                                  help_text='Пользователь',
                                  related_name='+',
                                  on_delete=models.CASCADE,
                                  blank=True,
                                  null=True
                                  )
    last_name = models.CharField(max_length=100, help_text='Фамилия')
    first_name = models.CharField(max_length=100, help_text='Имя')
    patronymic = models.CharField(max_length=100, help_text='Отчество', blank=True)
    url_facebook = models.URLField(help_text='Страница Facebook', blank=True)
    url_instagram = models.URLField(help_text='Страница Instagram', blank=True)
    url_vk = models.URLField(help_text='Страница VK', blank=True)
    url_youtube = models.URLField(help_text='Страница YouTube', blank=True)
    scan_id = models.FileField(help_text='Скан паспорта', blank=True)
    health_insurance_id = models.FileField(help_text='Скан медициской страховки', blank=True)
    sport_insurance_id = models.FileField(help_text='Скан спортивной страховки', blank=True)

    def __str__(self):
        return f'{str(self.last_name)} {self.first_name} ({self.person})'

    def image_tag(self):
        return mark_safe('<img src="{}" height="20"/>'.format(self.person.photo.url))

    image_tag.short_description = 'Image'


class Judge(models.Model):
    person = models.OneToOneField(Person,
                                  help_text='Пользователь',
                                  related_name='+',
                                  on_delete=models.CASCADE,
                                  blank=True,
                                  null=True
                                  )
    last_name = models.CharField(max_length=100, help_text='Фамилия')
    first_name = models.CharField(max_length=100, help_text='Имя')
    patronymic = models.CharField(max_length=100, help_text='Отчество', blank=True)
    position = models.CharField(max_length=100, help_text='Должность')
    facsimile = models.ImageField(help_text='Факсимиле', blank=True)
    is_admin = models.BooleanField(help_text='Администратор', default=False)

    def __str__(self):
        return f'{str(self.last_name)} {self.first_name} ({self.person})'