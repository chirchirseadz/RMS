# Generated by Django 3.2.9 on 2023-04-13 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('rentpayments', '0002_alter_manualrentpayments_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpesaonlinepayments',
            name='tenant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile'),
        ),
        migrations.AlterField(
            model_name='mpesaonlinepayments',
            name='update_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved')], default='pending', max_length=10),
        ),
        migrations.AlterUniqueTogether(
            name='mpesaonlinepayments',
            unique_together={('tenant', 'rent_details')},
        ),
        migrations.AlterUniqueTogether(
            name='rentdetails',
            unique_together={('year', 'pay_for_month')},
        ),
        migrations.DeleteModel(
            name='ManualRentPayments',
        ),
    ]
