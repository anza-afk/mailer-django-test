import os
import celerysettings
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailer.settings')

app = Celery('mail_factory')
app.config_from_object(celerysettings)
app.autodiscover_tasks()
