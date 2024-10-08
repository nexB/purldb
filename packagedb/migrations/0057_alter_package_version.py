# Generated by Django 4.1.2 on 2023-05-05 22:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("packagedb", "0056_rename_requirement_dependentpackage_extracted_requirement"),
    ]

    operations = [
        migrations.AlterField(
            model_name="package",
            name="version",
            field=models.CharField(
                blank=True, help_text="Version of the package.", max_length=100
            ),
        ),
    ]
