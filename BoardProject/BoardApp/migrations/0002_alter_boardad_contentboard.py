# Generated by Django 4.2.1 on 2023-05-21 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BoardApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardad',
            name='contentBoard',
            field=models.TextField(blank=True, help_text='Текст', verbose_name='Статья'),
        ),
    ]
