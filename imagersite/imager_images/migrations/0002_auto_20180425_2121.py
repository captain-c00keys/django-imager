# Generated by Django 2.0.4 on 2018-04-25 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='date_uploaded',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='product',
            new_name='album',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='date_uploaded',
            new_name='date_created',
        ),
        migrations.RemoveField(
            model_name='album',
            name='price',
        ),
        migrations.AlterField(
            model_name='album',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to=settings.AUTH_USER_MODEL),
        ),
    ]
