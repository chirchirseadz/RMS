# Generated by Django 4.1.7 on 2023-03-08 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartments',
            name='description',
            field=models.TextField(null=True),
        ),
    ]