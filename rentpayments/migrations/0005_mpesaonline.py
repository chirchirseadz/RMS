# Generated by Django 3.2.9 on 2023-03-27 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('rentpayments', '0004_remove_rentpayments_error_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='MpesaOnline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MerchantRequestID', models.CharField(blank=True, max_length=155, null=True)),
                ('CheckoutRequestID', models.CharField(blank=True, max_length=155, null=True)),
                ('ResultCode', models.CharField(blank=True, max_length=100, null=True)),
                ('ResultDesc', models.CharField(blank=True, max_length=100, null=True)),
                ('Amount', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('MpesaReceiptNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('TransactionDate', models.CharField(blank=True, max_length=55, null=True)),
                ('PhoneNumber', models.CharField(blank=True, max_length=25, null=True)),
                ('update_status', models.CharField(choices=[('recieved', 'Recieved'), ('updated', 'Updated')], default='recieved', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
            options={
                'verbose_name': 'Mpesa Online Payments',
                'verbose_name_plural': 'Mpesa Online Payments',
            },
        ),
    ]