from django.db import models
from django.utils.safestring import mark_safe


class Pond(models.Model):
    name = models.CharField(max_length=100, help_text='Название водоема')
    zone = models.CharField(max_length=3, help_text='Зона')
    width_bottom = models.DecimalField(help_text='Ширина (нижняя граница)', max_digits=15, decimal_places=3)
    width_top = models.DecimalField(help_text='Ширина (верхняя граница)', max_digits=15, decimal_places=3)
    max_depth = models.DecimalField(help_text='Максимальная глубина (м)', max_digits=15, decimal_places=3)
    avg_depth = models.DecimalField(help_text='Средняя глубина (м)', max_digits=15, decimal_places=3)
    square = models.DecimalField(help_text='Площадь (га)', max_digits=15, decimal_places=3)
    fish_density = models.DecimalField(help_text='Плотность рыбы (кг/га)', max_digits=15, decimal_places=3)
    avg_fish_weight = models.DecimalField(help_text='Средний вес рыбы (кг)', max_digits=15, decimal_places=3)
    description = models.TextField(help_text='Описание водоема')
    logo = models.ImageField(help_text='Логотип водоема', blank=True)
    address = models.TextField(help_text='Адрес', blank=True)
    width = models.DecimalField(help_text='Ширина водоема', max_digits=10, decimal_places=2)
    sector_width = models.DecimalField(help_text='Ширина водоема', max_digits=10, decimal_places=2)
    cell_height = models.IntegerField(help_text='Высота ячейки (dp)')

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" height="20"/>'.format(self.logo.url))

    image_tag.short_description = 'Image'


class Sector(models.Model):
    pond = models.ForeignKey(Pond, related_name='sectors', on_delete=models.CASCADE, help_text='Водоем')
    number = models.IntegerField(help_text='Номер сектора')

    class Meta:
        unique_together = ['pond', 'number']

    def __str__(self):
        return f'{self.number} ({self.pond})'
