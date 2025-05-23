# Generated by Django 4.2.11 on 2025-05-14 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('year_released', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('length', models.CharField(max_length=200)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.artist'),
        ),
    ]
