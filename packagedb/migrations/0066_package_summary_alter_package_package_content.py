# Generated by Django 4.1.2 on 2023-05-19 23:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("packagedb", "0065_set_package_content_field"),
    ]

    operations = [
        migrations.AddField(
            model_name="package",
            name="summary",
            field=models.JSONField(
                blank=True,
                default=dict,
                help_text="A mapping containing a summary and license clarity score for this Package",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="package",
            name="package_content",
            field=models.IntegerField(
                choices=[
                    (1, "curation"),
                    (2, "patch"),
                    (3, "source_repo"),
                    (4, "source_archive"),
                    (5, "binary"),
                    (6, "test"),
                    (7, "doc"),
                ],
                help_text="Content of this Package as one of: curation, patch, source_repo, source_archive, binary, test, doc",
                null=True,
            ),
        ),
    ]
