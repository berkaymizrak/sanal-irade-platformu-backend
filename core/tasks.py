# user/tasks.py
from celery import shared_task
from django.conf import settings
from django.core.management import call_command
from django.contrib.admin.models import LogEntry
