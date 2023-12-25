from time import sleep

from celery import Celery, shared_task
from datetime import timedelta
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'h_dubbed.settings')

app = Celery('h_dubbed', broker='redis://localhost:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.result_backend = 'redis://localhost:6379/0'

app.conf.task_serializer = 'json'
app.conf.result_serializer = 'pickle'
app.conf.accept_content = ['json', 'pickle']
app.conf.result_expires = timedelta(days=1)
app.conf.task_always_eager = False
app.conf.worker_prefetch_multiplier = 4
app.conf.CELERY_TRACK_STARTED = True

# app.conf.broker_url = 'amqp://'
# app.conf.result_backend = 'rpc://'


