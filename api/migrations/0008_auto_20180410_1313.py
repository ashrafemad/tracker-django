# Generated by Django 2.0.3 on 2018-04-10 13:13

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20180410_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=stdimage.models.StdImageField(blank=True, upload_to='big/'),
        ),
    ]