# Generated by Django 4.2.11 on 2025-05-14 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='length',
            field=models.DurationField(),
        ),
    ]
