# -*- coding: utf-8 -*-
from django import forms

from models import Client, EmailTemplate
from datetime import datetime
from time import localtime

class MailForm(forms.Form):
    client_choices = Client.objects.all().values_list('email', 'email',)
    recipient = forms.MultipleChoiceField(
        label='Получатели:',
        choices=client_choices,
        widget=forms.SelectMultiple(
            attrs={'style': 'width: 300px;', 'class': 'form-control'}
            ),
        initial=[x.email for x in Client.objects.all()]
        )
    subject = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Тема', 'style': 'width: 300px;', 'class': 'form-control'}
            )
        )
    message = forms.CharField(
        widget=forms.Textarea(
        attrs={'placeholder': 'Сообщение (опционально)', 'style': 'width: 500px;', 'class': 'form-control'}
        ),
        required=False
        )
    template = forms.ModelChoiceField(
        EmailTemplate.objects.all(),
        label='Выбор шаблона:',
        widget=forms.Select(attrs={
            'style': 'width: 300px;',
            'class': 'form-control'
            }),
        required=True
        )
    send_time = forms.DateTimeField(
        label='Дата и время отправки:',
        input_formats=['%d-%m-%Y %H:%M'],
        widget=forms.TextInput(
            {'placeholder': '{}'.format(datetime.now().strftime('%d-%m-%Y %H:%M')),
            'style': 'width: 300px;',
            'class': 'form-control'}),
        initial=datetime.now().strftime('%d-%m-%Y %H:%M'),
    )
