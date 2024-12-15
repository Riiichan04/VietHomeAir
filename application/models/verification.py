from django.db import models

from application.models import Account


class Verification(models.Model):
    code = models.CharField(max_length=10, unique=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()
    verify_type = models.CharField(max_length=5, choices=(('phone', 'Phone'), ('email', 'Email')))