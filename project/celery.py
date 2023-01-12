import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

appp = Celery('project')
appp.config_from_object('django.conf:settings', namespace='CELERY')

appp.autodiscover_tasks()