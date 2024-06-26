# Generated by Django 5.0.1 on 2024-03-29 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_time', models.TimeField(unique=True)),
            ],
            options={
                'ordering': ['slot_time'],
            },
        ),
        migrations.AddField(
            model_name='doctor',
            name='available_slots',
            field=models.ManyToManyField(blank=True, to='accounts.timeslot'),
        ),
    ]
