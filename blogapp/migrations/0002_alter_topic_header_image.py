# Generated by Django 4.0 on 2022-09-25 16:53

import blogapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='header_image',
            field=models.ImageField(null=True, upload_to=blogapp.models.topic_images_path),
        ),
    ]
