# Generated by Django 3.2.9 on 2023-03-14 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userprofile',
            unique_together={('apartment', 'room')},
        ),
    ]