import os
import time
from core.config import Settings
from celery import Celery


app_celery = Celery(
    backend = Settings.CELERY_RESULT_BACKEND,
    broker = Settings.CELERY_BROKER_URL
)

app_celery.conf.update(task_track_started=True)