# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.sites.models import Site
from django.contrib import admin
from .models import Client, MailingList, EmailTemplate
# Register your models here.
admin.site.register(Client)
admin.site.register(MailingList)
admin.site.register(EmailTemplate)
admin.site.unregister(Site)