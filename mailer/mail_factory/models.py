# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.conf import settings
from django.template.loader import render_to_string
from jsonfield import JSONField
# from django.utils.translation import activate 
class Client(models.Model):
    email = models.EmailField(max_length=254, db_index=True, null=False)
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    patronymic = models.CharField(max_length=250)
    date_of_birth = models.DateField()

    def __unicode__(self):
        return "{0} {1} {2}, {3}".format(self.surname, self.name, self.patronymic, self.email)

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class EmailTemplate(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    class Meta:
        verbose_name = 'шаблон'
        verbose_name_plural = 'шаблоны'
    

    def __unicode__(self):
        return self.title
    

class MailingList(models.Model):
    subject = models.CharField(max_length=500, null=True)
    mailing_time = models.DateTimeField('дата и время отправки')
    message = models.TextField(null=True)
    opened = JSONField(null=True)
    client = models.ManyToManyField(
        Client,
        verbose_name="Клиент"
    )
    template = models.ForeignKey(
        EmailTemplate,
        default=''
    )

    def __unicode__(self):
        return "{0} - {1}".format(self.subject, self.mailing_time)


    def send(self):
        client_query = self.client.all()
       
        for client in client_query:
            html_message = render_to_string(self.template.content, {'client': client})
            message = EmailMultiAlternatives(
                subject=self.subject,
                body=self.message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=(client.email,),
                )
            message.attach_alternative(html_message, "text/html")
            message.send(fail_silently=False)

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'

