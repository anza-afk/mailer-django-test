# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


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


class Mail(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'
    
    def __unicode__(self):
        return self.title


class MailingList(models.Model):
    mailing_time = models.DateTimeField('дата и время отправки')
    client = models.ManyToManyField(
        Client,
        verbose_name="Клиент"
    )
    mail = models.OneToOneField(
        Mail,
        on_delete=models.CASCADE,
    )

    def __unicode__(self):
        return "{0} {1}".format(self.mail.title, self.mailing_time)

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'

