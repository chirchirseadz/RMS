# Generated by Django 3.2.9 on 2023-03-13 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0007_alter_complaints_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='reported_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='your Username'),
        ),
    ]
