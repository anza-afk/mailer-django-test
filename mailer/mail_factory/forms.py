from django import forms
from models import Client,EmailTemplate
from django.contrib.admin import widgets
import datetime
from time import localtime

class MailForm(forms.Form):
    client_choices = Client.objects.all().values_list('email', 'email',)
    recipient = forms.MultipleChoiceField(choices=client_choices)  # , widget=forms.CheckboxSelectMultiple
    subject = forms.CharField(required=True)
    template = forms.ModelChoiceField(EmailTemplate.objects.all(), required=True)
    send_time = forms.DateTimeField(
        input_formats=['%d-%m-%Y %H:%M'],
        initial=datetime.datetime.now().strftime('%d-%m-%Y %H:%M'),
        label='t: ',
        help_text='%d-%m-%Y %H:%M',)
