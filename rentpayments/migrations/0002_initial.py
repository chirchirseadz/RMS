# Generated by Django 3.2.9 on 2023-03-24 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('rentpayments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentpayments',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile'),
        ),
        migrations.AddField(
            model_name='rentpayments',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentpayments.year'),
        ),
    ]