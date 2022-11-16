# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Client, MailingList, Mail
# Register your models here.
admin.site.register(Client)
admin.site.register(MailingList)
admin.site.register(Mail)