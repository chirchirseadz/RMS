# Generated by Django 3.2.9 on 2023-04-14 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentpayments', '0007_rentpayments_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentpayments',
            name='status',
        ),
    ]
