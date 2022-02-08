from django.db import models
from django.utils.safestring import mark_safe


class Team(models.Model):
    name = models.CharField(max_length=100, help_text='Название команды', blank=False)
    external_code = models.CharField(max_length=9, help_text='Код из 1С', blank=False)
    pin = models.CharField(max_length=4, help_text='Пин-код')
    logo = models.ImageField(help_text='Лого команды', blank=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" height="20"/>'.format(self.logo.url))

    image_tag.short_description = 'Image'