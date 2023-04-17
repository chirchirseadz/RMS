# Generated by Django 3.2.9 on 2023-04-12 16:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_for_month', models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=20)),
                ('status', models.CharField(choices=[('refunded', 'Refunded'), ('open', 'open'), ('closed', 'closed')], default='open', max_length=15, null=True)),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('due_date', models.DateTimeField(null=True)),
                ('cleared', models.BooleanField(default=False, null=True)),
                ('added', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Rent Details',
            },
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RentPayments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_on', models.DateField(auto_created=True, blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('approved', 'Approved'), ('pending', 'Pending')], default='Pending', max_length=15)),
                ('confirmed', models.BooleanField(default=False)),
                ('added_on', models.DateTimeField(default=datetime.datetime.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('rent_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rentpayments.rentdetails')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.rooms')),
                ('tenant', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
            options={
                'verbose_name_plural': 'Rent Payments',
            },
        ),
        migrations.AddField(
            model_name='rentdetails',
            name='year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='rentpayments.year'),
        ),
        migrations.CreateModel(
            name='MpesaOnlinePayments',
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
                ('rent_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='rentpayments.rentdetails')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
            options={
                'verbose_name': 'Mpesa Online Payments',
                'verbose_name_plural': 'Mpesa Online Payments',
            },
        ),
        migrations.CreateModel(
            name='ManualRentPayments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_on', models.DateField(auto_created=True, blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('approved', 'Approved'), ('pending', 'Pending')], default='Pending', max_length=15)),
                ('confirmed', models.BooleanField(default=False)),
                ('added_on', models.DateTimeField(default=datetime.datetime.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('rent_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rentpayments.rentdetails')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.rooms')),
                ('tenant', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
            options={
                'verbose_name_plural': 'Rent Payments',
            },
        ),
    ]
