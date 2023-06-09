# Generated by Django 3.2.9 on 2023-04-13 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
        ('users', '0001_initial'),
        ('rentpayments', '0003_auto_20230413_2345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mpesaonlinepayments',
            old_name='rent_details',
            new_name='RentDetails',
        ),
        migrations.AddField(
            model_name='mpesaonlinepayments',
            name='Room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.rooms'),
        ),
        migrations.AlterUniqueTogether(
            name='mpesaonlinepayments',
            unique_together={('tenant', 'RentDetails')},
        ),
    ]
