from celery import Celery
from datetime import timedelta
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'h_dubbed.settings')

app = Celery('h_dubbed')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# celery_app.conf.broker_url = 'amqp://'
# celery_app.conf.result_backend = 'rpc://'
app.conf.task_serializer = 'json'
app.conf.result_serializer = 'pickle'
app.conf.accept_content = ['json', 'pickle']
app.conf.result_expires = timedelta(days=1)
app.conf.task_always_eager = False
app.conf.worker_prefetch_multiplier = 4
