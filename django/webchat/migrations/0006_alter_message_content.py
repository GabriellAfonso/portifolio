# Generated by Django 5.0.2 on 2024-04-04 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webchat', '0005_rename_user_name_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(max_length=1000),
        ),
    ]