# Generated by Django 3.1.5 on 2021-01-31 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20210131_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shipped_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
    ]
