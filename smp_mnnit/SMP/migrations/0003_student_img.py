# Generated by Django 3.0.3 on 2020-05-27 14:19

import SMP.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMP', '0002_auto_20200526_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='img',
            field=models.ImageField(default='', upload_to=SMP.models.get_image_path),
        ),
    ]
