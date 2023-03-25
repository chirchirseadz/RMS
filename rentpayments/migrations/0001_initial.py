# Generated by Django 3.2.9 on 2023-03-24 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
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
                ('month', models.CharField(choices=[('JAN', 'January'), ('FEB', 'February'), ('MAR', 'March'), ('APR', 'April'), ('MAY', 'May'), ('JUN', 'June'), ('JUL', 'July'), ('AUG', 'August'), ('SEP', 'September'), ('OCT', 'October'), ('NOV', 'November'), ('DEC', 'December')], max_length=3)),
                ('phone_number', models.CharField(max_length=20)),
                ('amount', models.IntegerField()),
                ('account_reference', models.CharField(max_length=50)),
                ('transaction_desc', models.CharField(max_length=255)),
                ('callback_url', models.URLField(max_length=255)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], max_length=20)),
                ('transaction_id', models.CharField(blank=True, max_length=50, null=True)),
                ('error_message', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.rooms')),
            ],
        ),
    ]
