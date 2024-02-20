# Generated by Django 4.2.5 on 2024-02-19 13:33

from django.db import migrations, models
import webchat.models


class Migration(migrations.Migration):

    dependencies = [
        ('webchat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, to='webchat.profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='static/webchat/images/empty_picture.jpg', null=True, upload_to=webchat.models.get_profile_picture_path),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, max_length=225),
        ),
    ]
