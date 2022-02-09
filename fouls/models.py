from django.db import models
from django.utils.translation import gettext_lazy as _


class Foul(models.Model):
    class FoulType(models.TextChoices):
        WARNING = 'WR', _('Предупреждение')
        EXPELLING = 'EX', _('Дисквалификация')

    name = models.CharField(max_length=100, help_text='Название нарушения')
    external_code = models.CharField(max_length=9, help_text='Код из 1С')

    decision = models.CharField(
        max_length=2,
        choices=FoulType.choices,
        default=FoulType.WARNING,
    )

    def __str__(self):
        return self.name
