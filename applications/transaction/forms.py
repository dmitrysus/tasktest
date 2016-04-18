# -*- coding: utf-8 -*-

from django import forms
from applications.transaction.models import UserProfile


class TransactionForm(forms.Form):

    users = forms.ModelChoiceField(label='Пользователь', queryset=UserProfile.objects.all())
    vatins = forms.CharField(label='Список ИНН', widget=forms.Textarea)
    summ = forms.DecimalField(label='Сумма')

    def clean_summ(self):
        data = self.cleaned_data['summ']
        if self.cleaned_data.get('users'):
            if data > self.cleaned_data.get('users').account:
                raise forms.ValidationError("На счету пользователя недостаточно средств")
        return data

    def clean_vatins(self):
        data = self.cleaned_data['vatins']
        vatins_list = [vatin for vatin in data.replace(" ", "").split(",")]
        not_exist = []
        for vatin in vatins_list:
            if self.cleaned_data.get('users'):
                if vatin.isdigit():
                    if vatin == str(self.cleaned_data.get('users').vatin):
                        raise forms.ValidationError("Вы указали ИНН пользователя, со счета которого хотите снять средства")
                    elif not UserProfile.objects.filter(vatin=vatin):
                        not_exist.append(vatin)
                else:
                    raise forms.ValidationError("ИНН должен состоять только из цифр")

        if not_exist:
            raise forms.ValidationError("Пользователей о следующими ИНН не найдено: {}".format(str(not_exist)))
        return data
