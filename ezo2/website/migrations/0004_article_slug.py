# Generated by Django 2.0.3 on 2018-03-16 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20180316_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
