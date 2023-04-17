# Generated by Django 3.2.9 on 2023-04-17 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('rentpayments', '0020_remove_tenantrentpayments_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenantrentpayments',
            name='CheckoutRequestID',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tenantrentpayments',
            name='MerchantRequestID',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='tenantrentpayments',
            unique_together={('rent_details', 'tenant')},
        ),
    ]