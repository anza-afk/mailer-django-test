from django import forms
from models import Client, EmailTemplate
from django.contrib.admin import widgets
import datetime
from time import localtime

class MailForm(forms.Form):
    client_choices = Client.objects.all().values_list('email', 'email',)
    recipient = forms.MultipleChoiceField(choices=client_choices, initial=[x.email for x in Client.objects.all()])
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea,  required=False)
    template = forms.ModelChoiceField(EmailTemplate.objects.all(), required=True)
    send_time = forms.DateTimeField(
        input_formats=['%d-%m-%Y %H:%M'],
        initial=datetime.datetime.now().strftime('%d-%m-%Y %H:%M'),
        label='t: ',
        help_text='%d-%m-%Y %H:%M',)
