# Generated by Django 5.1.2 on 2024-11-25 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_user_session_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='session_token',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
