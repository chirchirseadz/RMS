# Generated by Django 3.2.9 on 2023-03-23 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0003_remove_rooms_tenant'),
        ('users', '0019_auto_20230323_0831'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userprofile',
            unique_together={('name', 'apartment')},
        ),
    ]
