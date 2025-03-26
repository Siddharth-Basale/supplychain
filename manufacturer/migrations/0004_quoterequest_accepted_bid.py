# Generated by Django 5.1.6 on 2025-03-25 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturer', '0003_quoterequest_status'),
        ('supplier', '0002_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='quoterequest',
            name='accepted_bid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='supplier.bid'),
        ),
    ]
