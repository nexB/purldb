# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-10 02:08
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packagedb', '0007_auto_20180713_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='package_url',
            field=models.CharField(blank=True, db_index=True, help_text='Package URL for this resource. It stands for a package "mostly universal" URL.', max_length=2048, null=True),
        ),
    ]
