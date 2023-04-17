# Generated by Django 3.2.9 on 2023-04-16 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentpayments', '0017_tenantrentpayments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentdetails',
            name='end_date',
        ),
        migrations.AlterField(
            model_name='tenantrentpayments',
            name='paid_on',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]