# Generated by Django 5.1.3 on 2025-01-08 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_alter_account_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='note',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
