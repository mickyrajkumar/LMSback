# Generated by Django 4.0.4 on 2022-06-02 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_borrow_submit_alter_borrow_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 17, 21, 46, 54, 951575)),
        ),
    ]
