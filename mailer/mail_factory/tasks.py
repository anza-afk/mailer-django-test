# -*- coding: utf-8 -*-
import string

from celery import shared_task
from django.contrib.sites.models import Site
from django.urls import reverse
from models import MailingList
from datetime import datetime
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task(name='send_db_emails')
def send_db_emails():
    url = "%s%s" % (Site.objects.get_current().domain, reverse('image_load'))
    mailing_list = MailingList.objects.filter(sent=False).filter(mailing_time__lte=datetime.now())
    for mail in mailing_list:
        mail.send(url)
        logger.info('all mail for {} sent!'.format(mail.subject).encode('UTF-8'))
