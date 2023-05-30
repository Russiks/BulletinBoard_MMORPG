from celery import shared_task
import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import BoardAd

# Еженедельная рассылка новых объявлений
@shared_task
def mail_every_task():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    ads = BoardAd.objects.filter(dateCreation__gte=last_week)
    users = set(User.objects.all().values_list('email', flat=True))
    html_content = render_to_string(
        'BoardApp/weekly_ad.html',
        {
            'link': settings.SITE_URL,
            'ads': ads,
        }
    )

    for email in users:
        send_mail(
            subject='Publications for the week',
            message='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            html_message=html_content,
        )


# Task на отправку уведомлений
@shared_task
def send_mail_task(subject, message, email):
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
        # fail_silently: Булево число. Когда это False, send_mail() вызовет smtplib.SMTPException, если произойдет
        # ошибка. Список возможных исключений см. в документации smtplib, все они являются подклассами SMTPException.

    )
