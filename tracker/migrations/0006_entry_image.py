# Generated by Django 2.0.3 on 2018-03-29 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_remove_entry_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]