# Generated by Django 4.0.4 on 2022-05-24 14:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_newuser_gender_alter_borrow_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 20, 2, 27, 757090)),
        ),
    ]
