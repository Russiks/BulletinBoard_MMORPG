from django.db import models
from django.contrib.auth.models import User


# Класс для авторизованных пользователей
class UsersAuth(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
    )
    code = models.SmallIntegerField(
        default=0,
    )

    def __str__(self):
        return f'#{self.id}. User: {self.user}'