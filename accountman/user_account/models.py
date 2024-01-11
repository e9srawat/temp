from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode = models.CharField(max_length=50, choices=[('credit', 'Credit'), ('debit', 'Debit')])

    def __str__(self):
        return self.user.username


class Transaction(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField()
    category = models.CharField(max_length=50, choices=[('food', 'Food'), ('travel', 'Travel'), ('entertainment', 'Entertainment'), ('rent', 'Rent')])
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.date} - {self.category}"
