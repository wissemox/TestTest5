# Generated by Django 3.1.11 on 2021-06-02 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0005_auto_20210510_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_banned',
            field=models.BooleanField(default=False),
        ),
    ]