# Generated by Django 5.0.7 on 2024-08-11 22:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_order_order_group_alter_order_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 11, 23, 19, 53, 410385, tzinfo=datetime.timezone.utc)),
        ),
    ]
