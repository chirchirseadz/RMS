# Generated by Django 3.2.9 on 2023-03-22 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0003_remove_rooms_tenant'),
        ('users', '0012_alter_userprofile_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='apartment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.apartments'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.rooms', verbose_name='Rented Room'),
        ),
        migrations.AlterUniqueTogether(
            name='userprofile',
            unique_together={('apartment', 'room')},
        ),
    ]
