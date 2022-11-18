# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import BadHeaderError
from .forms import MailForm
from django.conf import settings
from models import MailingList, Client
from django.core.exceptions import ObjectDoesNotExist


def image_load(request):
    """Эндпоинт, запрашиваемй при поткрытии объекса image в письме"""
    if request.GET.get('mailing'):
        mailing_list = MailingList.objects.get(id=request.GET.get('mailing'))
    if request.GET.get('client'):
        client = Client.objects.get(id=request.GET.get('client'))
    try:
        if mailing_list.opened:
            mailing_list.opened[client.id] = client.email
        else:
            mailing_list.opened = {client.id: client.email}
        mailing_list.save()
    except ObjectDoesNotExist:
        pass


def index(request):
    """Главная страница"""
    mail_sent = 'No'

    if request.method == "GET":
        form = MailForm()
    else:
        form = MailForm(request.POST)
        if form.is_valid():
            try:
                new_mailing_list = MailingList(
                    subject = form.cleaned_data['subject'],
                    message =  form.cleaned_data['message'],
                    mailing_time = form.cleaned_data['send_time']
                )

                new_mailing_list.template = form.cleaned_data['template']
                new_mailing_list.save()
                for recipient in form.cleaned_data['recipient']:
                    new_mailing_list.client.add(
                        Client.objects.filter(email=recipient).first())
                new_mailing_list.save()
                
                if 'send_email' in request.POST:
                    new_mailing_list.mailing_time = datetime.now()
                    new_mailing_list.save()
                    url = request.build_absolute_uri('image_load'),
                    new_mailing_list.send(url)
                    mail_sent = 'Yes'
                elif 'plan_email' in request.POST:
                    mail_sent = 'Planned'
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

    return render(request, 'email.html', {'form': form, 'mail_sent': mail_sent})
