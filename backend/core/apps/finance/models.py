from django.db import models

from core.apps.authentication.models import User
from core.apps.finance.choices import AccountType


class BankAccount(models.Model):
    account_name = models.CharField(max_length=150)
    account_number = models.CharField(max_length=150)
    account_type = models.CharField(max_length=15, choices=AccountType.choices)
    bank = models.CharField(max_length=150)
    branch = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bank_account')

    objects = models.Manager()

    class Meta:
        db_table = 'finance_bank_account'
        constraints = [
            models.UniqueConstraint(
                fields=['account_number', 'bank'],
                name='unique_bank_account',
            ),
        ]
