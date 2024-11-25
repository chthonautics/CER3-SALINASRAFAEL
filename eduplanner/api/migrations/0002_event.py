# Generated by Django 5.1.2 on 2024-11-22 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Evento', max_length=256)),
                ('description', models.CharField(default='', max_length=2048)),
                ('date_start', models.CharField(default='1970-1-1', max_length=16)),
                ('date_end', models.CharField(default='1970-1-1', max_length=16)),
                ('forced', models.BooleanField(default=False)),
                ('event_type', models.CharField(default='Evento', max_length=512)),
            ],
        ),
    ]
