import string

from celery import shared_task

from models import MailingList
from datetime import datetime
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task(name='send_db_emails')
def send_db_emails():
    # mailing_list = MailingList.objects.get(id=args[1])
    mailing_list = MailingList.objects.filter(sent=False).filter(mailing_time__lte=datetime.now())
    for mail in mailing_list:
        mail.send()
        logger.info('all mail for {} sent!'.format(mail.subject).encode("UTF-8"))
