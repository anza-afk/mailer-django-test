# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .forms import MailForm
from django.conf import settings
from models import MailingList, Client, EmailTemplate



# def index(request):
#     for filename in os.listdir(".\\templates\email_templates"):
#         print(filename)
#     # mail_templates = [i for i in email_templates]
#     return render(request, "index.html")

def index(request):
    
    mail_sent = False

    if request.method == "GET":
        form = MailForm()
    else:
        form = MailForm(request.POST)
        if form.is_valid():
            try:
                # new_mail = Mail(
                #     title = form.cleaned_data["subject"],
                #     content = form.cleaned_data['message']
                #     )
                # new_mail.save()

                new_mailing_list = MailingList(
                    subject = form.cleaned_data["subject"],
                    message =  form.cleaned_data["message"],
                    mailing_time = form.cleaned_data['send_time']
                )

                new_mailing_list.template = form.cleaned_data["template"]
                new_mailing_list.save()
                for recipient in form.cleaned_data["recipient"]:
                    new_mailing_list.client.add(Client.objects.filter(email=recipient).first())
                new_mailing_list.save()
                
                if 'send_email' in request.POST:
                    print('send_email', form.cleaned_data["template"].content)
                    new_mailing_list.send()
                    # send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, form.cleaned_data["recipient"] , fail_silently=False)
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            mail_sent = True
    return render(request, "email.html", {"form": form, 'mail_sent': mail_sent})



def template_test(request):
    client = Client.objects.all().first()
    return render(
        request,
        EmailTemplate.objects.filter(title='news').first().content,
        {"client": client})