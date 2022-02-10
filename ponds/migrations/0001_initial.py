# Generated by Django 3.2 on 2022-02-10 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название водоема', max_length=100)),
                ('zone', models.CharField(help_text='Зона', max_length=3)),
                ('width_bottom', models.DecimalField(decimal_places=3, help_text='Ширина (нижняя граница)', max_digits=15)),
                ('width_top', models.DecimalField(decimal_places=3, help_text='Ширина (верхняя граница)', max_digits=15)),
                ('max_depth', models.DecimalField(decimal_places=3, help_text='Максимальная глубина (м)', max_digits=15)),
                ('avg_depth', models.DecimalField(decimal_places=3, help_text='Средняя глубина (м)', max_digits=15)),
                ('square', models.DecimalField(decimal_places=3, help_text='Площадь (га)', max_digits=15)),
                ('fish_density', models.DecimalField(decimal_places=3, help_text='Плотность рыбы (кг/га)', max_digits=15)),
                ('avg_fish_weight', models.DecimalField(decimal_places=3, help_text='Средний вес рыбы (кг)', max_digits=15)),
                ('description', models.TextField(help_text='Описание водоема')),
                ('logo', models.ImageField(blank=True, help_text='Логотип водоема', upload_to='')),
                ('address', models.TextField(blank=True, help_text='Адрес')),
                ('width', models.DecimalField(decimal_places=2, help_text='Ширина водоема', max_digits=10)),
                ('sector_width', models.DecimalField(decimal_places=2, help_text='Ширина водоема', max_digits=10)),
                ('cell_height', models.IntegerField(help_text='Высота ячейки (dp)')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(help_text='Номер сектора')),
                ('pond', models.ForeignKey(help_text='Водоем', on_delete=django.db.models.deletion.CASCADE, related_name='sectors', to='ponds.pond')),
            ],
            options={
                'unique_together': {('pond', 'number')},
            },
        ),
    ]
