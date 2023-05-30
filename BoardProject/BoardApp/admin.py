from django.contrib import admin

from .models import (
    BoardAd, Feedback
)

admin.site.register(BoardAd)
admin.site.register(Feedback)

