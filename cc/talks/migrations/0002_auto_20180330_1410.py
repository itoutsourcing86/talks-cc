# Generated by Django 2.0.3 on 2018-03-30 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talklist',
            name='id',
        ),
        migrations.AlterField(
            model_name='talklist',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, primary_key=True, serialize=False),
        ),
    ]
