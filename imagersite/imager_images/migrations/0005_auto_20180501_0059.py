# Generated by Django 2.0.4 on 2018-05-01 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0004_auto_20180426_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='album',
        ),
        migrations.AddField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(related_name='albums', to='imager_images.Photo'),
        ),
    ]
