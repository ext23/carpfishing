from django.db import models
from django.utils.safestring import mark_safe


class Member(models.Model):

    last_name = models.CharField(max_length=100, help_text='Фамилия')
    first_name = models.CharField(max_length=100, help_text='Имя')
    patronymic = models.CharField(max_length=100, help_text='Отчество', blank=True)
    photo = models.ImageField(help_text='Фотография', blank=True)
    url_facebook = models.URLField(help_text='Страница Facebook', blank=True)
    url_instagram = models.URLField(help_text='Страница Instagram', blank=True)
    url_vk = models.URLField(help_text='Страница VK', blank=True)
    url_youtube = models.URLField(help_text='Страница YouTube', blank=True)
    scan_id = models.FileField(help_text='Скан паспорта', blank=True)
    health_insurance_id = models.FileField(help_text='Скан медициской страховки', blank=True)
    sport_insurance_id = models.FileField(help_text='Скан спортивной страховки', blank=True)
    external_code = models.CharField(max_length=9, help_text='Код из 1С')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    def image_tag(self):
        return mark_safe('<img src="{}" height="20"/>'.format(self.photo.url))

    image_tag.short_description = 'Image'
