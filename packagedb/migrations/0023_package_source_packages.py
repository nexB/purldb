# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-23 19:35
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packagedb', '0022_package_manifest_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='source_packages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, null=True), blank=True, default=list, help_text='A list of source package URLs (aka. "purl") for this package. For instance an SRPM is the "source package" for a binary RPM.', null=True, size=None),
        ),
    ]
