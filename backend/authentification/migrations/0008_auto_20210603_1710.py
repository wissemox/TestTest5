# Generated by Django 3.1.12 on 2021-06-03 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0007_user_time_ban'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='time_ban',
            new_name='end_time_ban',
        ),
    ]