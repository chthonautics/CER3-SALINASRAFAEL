# Generated by Django 5.1.2 on 2024-11-22 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='session_token',
            field=models.CharField(max_length=32),
        ),
    ]