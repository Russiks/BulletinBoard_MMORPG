# Generated by Django 4.2.1 on 2023-05-21 21:05

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleBoard', models.CharField(help_text='Max 128 symbols', max_length=128)),
                ('contentBoard', ckeditor.fields.RichTextField()),
                ('categoryBoard', models.CharField(choices=[('Tanks', 'Танки'), ('Heals', 'Хилы'), ('Damage Dealers', 'Дамаг Дилеры'), ('Traders', 'Торговцы'), ('Guild Master', 'Гилдмастеры'), ('Quests Givers', 'Квестгиверы'), ('Blacksmiths', 'Кузнецы'), ('Tanner', 'Кожевники'), ('Potion Makers', 'Зелевары'), ('Spell Masters', 'Мастера заклинаний')], default='Tanks', help_text='Category name', max_length=26, verbose_name='Category')),
                ('dateCreation', models.DateField(auto_now_add=True)),
                ('timeCreation', models.TimeField(auto_now_add=True)),
                ('author', models.ForeignKey(help_text='Author', on_delete=django.db.models.deletion.CASCADE, related_name='author_board', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textComment', models.TextField(help_text='Text comment', max_length=256)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('confirmComment', models.BooleanField(default=False)),
                ('author', models.ForeignKey(help_text='Author comment', on_delete=django.db.models.deletion.CASCADE, related_name='author_comment', to=settings.AUTH_USER_MODEL)),
                ('commentBoard', models.ForeignKey(help_text='Comment', on_delete=django.db.models.deletion.CASCADE, related_name='comment_by_ad', to='BoardApp.boardad')),
            ],
        ),
    ]
