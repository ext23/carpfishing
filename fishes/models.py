from django.db import models
from django.utils.safestring import mark_safe


class Fish(models.Model):
    name = models.CharField(max_length=100, help_text='Название рыбы')
    description = models.TextField(help_text='Описание')
    image = models.ImageField(help_text='Изображение', blank=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" height="20"/>'.format(self.image.url))

    image_tag.short_description = 'Image'