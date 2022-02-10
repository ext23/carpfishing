# Generated by Django 3.2 on 2022-02-10 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название рыбы', max_length=100)),
                ('external_code', models.CharField(help_text='Код из 1С', max_length=9)),
                ('description', models.TextField(help_text='Описание')),
                ('image', models.ImageField(blank=True, help_text='Изображение', upload_to='')),
            ],
        ),
    ]
