# Generated by Django 2.0.3 on 2018-04-10 12:17

import datetime
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=stdimage.models.StdImageField(default='', upload_to='big'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.date(2018, 4, 10)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date(2018, 4, 10)),
        ),
    ]