# Generated by Django 3.2.9 on 2023-04-14 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentpayments', '0005_auto_20230414_0123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentpayments',
            name='confirmed',
        ),
    ]
