from datetime import timezone

from django.db import models

from application.models import Account


class Verification(models.Model):
    code = models.CharField(max_length=10, unique=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    expired_at = models.DateTimeField(null=True)
    verify_type = models.CharField(max_length=5, choices=(('phone', 'Phone'), ('email', 'Email')))

    def is_expired(self):
        return self.expired_at and self.expired_at < timezone.now()