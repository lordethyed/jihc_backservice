# Generated by Django 5.0 on 2023-12-22 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_free',
            field=models.BooleanField(default=True),
        ),
    ]
