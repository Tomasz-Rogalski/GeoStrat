# Generated by Django 4.0 on 2022-09-25 16:55

import blogapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_topic_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='header_image',
            field=models.ImageField(blank=True, upload_to=blogapp.models.topic_images_path),
        ),
    ]
