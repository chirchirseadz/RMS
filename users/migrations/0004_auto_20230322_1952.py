# Generated by Django 3.2.9 on 2023-03-22 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20230322_1917'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userprofile',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='apartment',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='room',
        ),
    ]
