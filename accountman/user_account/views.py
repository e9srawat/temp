from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .models import UserProfile, Transaction
from .forms import TransactionForm
from django.http import HttpResponse
import csv

class UserProfileView(LoginRequiredMixin, FormView):
    template_name = 'user_account/user_profile.html'
    form_class = TransactionForm
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = self.request.user.userprofile
        transactions = Transaction.objects.filter(user_profile=user_profile)
        context['username'] = self.request.user.username
        context['account_balance'] = user_profile.account_balance
        context['payment_mode'] = user_profile.payment_mode
        context['transactions'] = transactions
        return context

    def form_valid(self, form):
        user_profile = self.request.user.userprofile
        form.instance.user_profile = user_profile
        form.save()
        return super().form_valid(form)

@login_required
def generate_report(request):
    user_profile = request.user.userprofile
    transactions = Transaction.objects.filter(user_profile=user_profile)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="transaction_report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Date', 'Category', 'Amount'])

    for transaction in transactions:
        writer.writerow([transaction.date, transaction.category, transaction.amount])

    return response
