from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from BoardApp.config.post_categories import CATEGORY_CHOICES


class BoardAd(models.Model):
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='author_board',
        help_text='Author',
    )

    titleBoard = models.CharField(
        max_length=128,
        help_text='Max 128 symbols',
    )

    contentBoard = RichTextField()

    categoryBoard = models.CharField(
        max_length=26,
        choices=CATEGORY_CHOICES,
        default='Tanks',
        help_text='Category name',
        verbose_name='Category',
    )

    dateCreation = models.DateField(
        auto_now_add=True,
    )

    timeCreation = models.TimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.titleBoard}'

    def get_absolute_url(self):
        return reverse('board_detail', args=[str(self.id)])


class Feedback(models.Model):
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='author_comment',
        help_text='Author comment',
    )

    commentBoard = models.ForeignKey(
        to=BoardAd,
        on_delete=models.CASCADE,
        related_name='comment_by_ad',
        help_text='Comment',
    )

    textComment = models.TextField(
        max_length=256,
        help_text='Text comment',
    )

    dateCreation = models.DateTimeField(
        auto_now_add=True,
    )

    confirmComment = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f'#{self.id}. Author: {self.author} Date: {self.dateCreation}'
