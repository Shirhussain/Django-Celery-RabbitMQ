from __future__ import absolute_import, unicode_literals 
import os 
from celery import Celery 

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
app = Celery('mysite')

app.autodiscover_tasks()

# to run our worker we need run the following command
# celery -A mysite worker -l INFO

