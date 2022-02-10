from django.db import models
from django.utils.safestring import mark_safe
from persons.models import Person


class Member(models.Model):
    person = models.OneToOneField(Person,
                                  help_text='Пользователь',
                                  related_name='+',
                                  on_delete=models.CASCADE,
                                  null=True)
    url_facebook = models.URLField(help_text='Страница Facebook', blank=True)
    url_instagram = models.URLField(help_text='Страница Instagram', blank=True)
    url_vk = models.URLField(help_text='Страница VK', blank=True)
    url_youtube = models.URLField(help_text='Страница YouTube', blank=True)
    scan_id = models.FileField(help_text='Скан паспорта', blank=True)
    health_insurance_id = models.FileField(help_text='Скан медициской страховки', blank=True)
    sport_insurance_id = models.FileField(help_text='Скан спортивной страховки', blank=True)
    external_code = models.CharField(max_length=9, help_text='Код из 1С')

    def __str__(self):
        return f'{str(self.person)}'

    def image_tag(self):
        return mark_safe('<img src="{}" height="20"/>'.format(self.person.photo.url))

    image_tag.short_description = 'Image'
