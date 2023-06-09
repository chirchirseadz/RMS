# Generated by Django 3.2.9 on 2023-03-24 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllocateRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allocate_date', models.DateField(auto_created=True, null=True)),
                ('paid', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True)),
                ('approved', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True, null=True)),
                ('priority', models.CharField(choices=[('High Priority', 'High Priority'), ('Medium Priority', 'Medium Priority'), ('Less Priority', 'Less Priority')], max_length=100, null=True)),
                ('subject', models.CharField(blank=True, help_text='other type of isses...', max_length=100, null=True)),
                ('status', models.CharField(choices=[('Received', 'Received'), ('Processing', 'Processing'), ('Resolved', 'Resolved'), ('Dropped', 'Dropped')], max_length=20, null=True)),
                ('description', models.TextField(null=True, verbose_name='Describe the situation')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Complaints',
            },
        ),
        migrations.CreateModel(
            name='MessagesFromTenants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('message_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Messages From Tenants',
            },
        ),
        migrations.CreateModel(
            name='NoticesToTenants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_date', models.DateField(auto_created=True, null=True)),
                ('notice_date', models.DateTimeField(auto_created=True)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'NoticesToTenants',
            },
        ),
        migrations.CreateModel(
            name='RoomBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_by', models.CharField(max_length=40, null=True, verbose_name='Your Name')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Your Email Address')),
                ('phone_number', models.CharField(max_length=13, null=True, verbose_name='Active Phone Number.')),
                ('request_info', models.TextField(blank=True, help_text='Your Request Information', max_length=100, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Already Sorted', 'Already Sorted')], default='Pending', max_length=100, null=True)),
                ('date_requested', models.DateTimeField(auto_now=True)),
                ('room_booked', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.rooms')),
            ],
        ),
    ]
