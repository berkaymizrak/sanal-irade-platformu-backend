import os
import django

from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program. Change `sanal_irade_platformu` with your project name.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sanal_irade_platformu.settings')
django.setup()

# Change `sanal_irade_platformu` with your project name.
app = Celery('sanal_irade_platformu')

app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
