# Generated by Django 3.2.9 on 2023-03-23 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_allocateroom_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allocateroom',
            old_name='disalloacate_date',
            new_name='alloacate_date',
        ),
    ]