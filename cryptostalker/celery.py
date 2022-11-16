from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptostalker.settings')

app = Celery('cryptostalker')

app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {

    'save crypto values':{
        'task':'base.tasks.save_to_database',
        'schedule': 60*5, # scheduled for every 5 minutes
        #'args': ()
    },

}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')