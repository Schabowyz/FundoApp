# Generated by Django 4.2.3 on 2023-07-25 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0008_alter_payment_datetime_tokens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 25, 16, 5, 59, 182318, tzinfo=datetime.timezone.utc)),
        ),
    ]