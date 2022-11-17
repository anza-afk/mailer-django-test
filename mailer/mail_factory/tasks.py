import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task

from models import MailingList
from datetime import datetime

@shared_task
def send_db_emails():
    # mailing_list = MailingList.objects.get(id=args[1])
    mailing_list = MailingList.objects.filter(mailing_time__lte=datetime.now())
    mailing_list.send()
    return 'all mail for {} sent!'.format(mailing_list.subject).encode("UTF-8")