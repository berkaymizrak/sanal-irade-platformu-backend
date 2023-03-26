from celery import shared_task
from django.conf import settings
from django.core.management import call_command
from django.contrib.admin.models import LogEntry
from mailqueue.models import MailerMessage


@shared_task
def send_mail_queued(mail_subject, message_context, to, from_mail=settings.DEFAULT_FROM_EMAIL,
                     reply_to=None, cc=None, bcc=None, ):
    msg = MailerMessage()
    msg.subject = mail_subject
    msg.to_address = to

    # For sender names to be displayed correctly on mail clients, simply put your name first
    # and the actual email in angle brackets
    # Example correct sender value "Dave Johnston <dave@example.com>"
    msg.from_address = from_mail

    # As this is only an example, we place the text content in both the plaintext version (content)
    # and HTML version (html_content).
    msg.content = message_context
    message_html = message_context.replace('\n', '<br>')
    msg.html_content = message_html

    if cc:
        msg.cc_address = cc
    if bcc:
        msg.bcc_address = bcc
    if reply_to:
        msg.reply_to = reply_to

    # Name of your App that is sending the email.
    msg.app = 'Sanal İrade Platformu'

    msg.save()


@shared_task
def command_send_queued_messages():
    # The management command for sending queued messages.
    # Command comes with mailqueue package.
    call_command('send_queued_messages')


@shared_task
def command_clear_expired_sessions():
    # The management command for clearing expired sessions from Session model of django.contrib.sessions package.
    # This is a built-in management command of Django.
    # Suggested to use frequently to clear expired sessions based on number of guests you have.
    call_command('clearsessions')


@shared_task
def command_clear_sent_messages():
    # The management command for clearing sent messages from MailerMessage model of mailqueue package.
    # Command comes with mailqueue package.
    call_command('clear_sent_messages')


@shared_task
def clear_admin_logs(leave_last=100):
    # The management command for clearing admin logs from LogEntry model of django.contrib.admin package.
    # leave_last is the number of the latest logs to keep.
    """
        # Set Arguments as:
        {
        'leave_last' : 100
        }
    """
    model_say = LogEntry.objects.count()
    if model_say > leave_last:
        rows = LogEntry.objects.all()[:leave_last].values_list('id', flat=True)  # only retrieve ids.
        LogEntry.objects.exclude(pk__in=list(rows)).delete()
