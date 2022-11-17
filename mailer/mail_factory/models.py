# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail, BadHeaderError
from django.db import models
from django.conf import settings
from django.template.loader import render_to_string


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
    message = models.TextField()
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
        client_list = [x.email for x in self.client]
        for client in client_list:
            html_message = render_to_string(self.template, {'client': client})
            send_mail(
                subject=self.subject,
                message=self.message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=client_list,
                fail_silently=False,
                html_message=self.html_message
                )

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'

