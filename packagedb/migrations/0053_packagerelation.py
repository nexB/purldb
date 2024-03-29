# Generated by Django 4.1.2 on 2023-04-01 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("packagedb", "0052_package_index_error_package_last_indexed_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="PackageRelation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "relationship",
                    models.CharField(
                        choices=[("source_package", "Source Package")],
                        help_text='Relationship between the from and to package URLs such as "source_package" when a package is the source code package for another package.',
                        max_length=30,
                    ),
                ),
                (
                    "from_package",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_to",
                        to="packagedb.package",
                    ),
                ),
                (
                    "to_package",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_from",
                        to="packagedb.package",
                    ),
                ),
            ],
        ),
    ]
