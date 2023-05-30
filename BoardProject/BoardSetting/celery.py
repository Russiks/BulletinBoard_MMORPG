import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BoardSetting.settings')

app = Celery('BoardApp')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'weekle_ad_every_monday': {
        'task': 'BoardApp.tasks.mail_every_task',
        'schedule': crontab(day_of_week="monday", hour=9, minute=0),
    },
}