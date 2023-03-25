# Generated by Django 3.2.9 on 2023-03-24 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
        ('users', '0001_initial'),
        ('rentpayments', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentpayments',
            name='account_reference',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='rentpayments',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='rentpayments',
            name='callback_url',
            field=models.URLField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rentpayments',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='rentpayments',
            name='month',
            field=models.CharField(choices=[('JAN', 'January'), ('FEB', 'February'), ('MAR', 'March'), ('APR', 'April'), ('MAY', 'May'), ('JUN', 'June'), ('JUL', 'July'), ('AUG', 'August'), ('SEP', 'September'), ('OCT', 'October'), ('NOV', 'November'), ('DEC', 'December')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='rentpayments',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rentpayments',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.rooms'),
        ),
        migrations.AlterField(
            model_name='rentpayments',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rentpayments',
            name='tenant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile'),
        ),
        migrations.AlterField(
            model_name='rentpayments',
            name='transaction_desc',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rentpayments',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='rentpayments',
            name='year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rentpayments.year'),
        ),
    ]
