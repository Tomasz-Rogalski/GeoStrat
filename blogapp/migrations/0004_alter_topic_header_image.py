# Generated by Django 4.0 on 2022-09-26 09:56

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_alter_topic_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='header_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
