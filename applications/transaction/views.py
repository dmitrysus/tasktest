# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

from applications.transaction.forms import TransactionForm
from applications.transaction.models import UserProfile


def transactions_page(request):
    form = TransactionForm()
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            bank_user = form.cleaned_data['users']
            bank_user.account = bank_user.account - form.cleaned_data['summ']
            bank_user.save()
            vatins_list = [vatin for vatin in form.cleaned_data['vatins'].replace(" ", "").split(",")]
            users_to_pay = UserProfile.objects.filter(vatin__in=vatins_list)
            for user in users_to_pay:
                user.account += form.cleaned_data['summ']/len(users_to_pay)
                user.save()
    ctx = {
        'form': form,
        'users': UserProfile.objects.all(),

    }

    return render_to_response('transactions_page.html', ctx, context_instance=RequestContext(request))
