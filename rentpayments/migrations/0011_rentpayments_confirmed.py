# Generated by Django 3.2.9 on 2023-04-14 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentpayments', '0010_remove_rentpayments_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentpayments',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
