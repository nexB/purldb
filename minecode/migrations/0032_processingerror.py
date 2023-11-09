# Generated by Django 4.1.2 on 2023-11-06 19:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("minecode", "0031_importableuri"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProcessingError",
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
                    "uri",
                    models.CharField(
                        db_index=True,
                        help_text="URI for this resource. This is the unmodified original URI.",
                        max_length=2048,
                    ),
                ),
                (
                    "canonical",
                    models.CharField(
                        db_index=True,
                        help_text="Canonical form of the URI for this resource that must be unique across all ResourceURI.",
                        max_length=3000,
                    ),
                ),
                (
                    "source_uri",
                    models.CharField(
                        blank=True,
                        help_text="Optional: real source remote URI for this visit.For example for a package repository index is a typical source via which a first level of package data is fetched. And it is not the URI in the uri field. It is just the source of the fetchOr the source may be a mirror URI used for fetching.",
                        max_length=2048,
                        null=True,
                    ),
                ),
                (
                    "priority",
                    models.PositiveIntegerField(
                        db_index=True,
                        default=0,
                        help_text="Absolute procdssing priority of a URI (default to zero), higher number means higher priority, zero means lowest priority.",
                    ),
                ),
                (
                    "wip_date",
                    models.DateTimeField(
                        blank=True,
                        db_index=True,
                        help_text="Work In Progress. This is a timestamp set at the start of a visit or mapping or indexing or null when no processing is in progress.",
                        null=True,
                    ),
                ),
                (
                    "file_name",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        help_text="File name of a resource sometimes part of the URI proper and sometimes only available through an HTTP header.",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "size",
                    models.PositiveIntegerField(
                        blank=True,
                        db_index=True,
                        help_text="Size in bytes of the file represented by this ResourceURI.",
                        null=True,
                    ),
                ),
                (
                    "sha1",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        help_text="SHA1 checksum hex-encoded (as in the sha1sum command) of the content of the file represented by this ResourceURI.",
                        max_length=40,
                        null=True,
                    ),
                ),
                (
                    "md5",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        help_text="MD5 checksum hex-encoded (as in the md5sum command) of the content of the file represented by this ResourceURI.",
                        max_length=32,
                        null=True,
                    ),
                ),
                (
                    "sha256",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        help_text="SHA256 checksum hex-encoded (as in the sha256sum command) of the content of the file represented by this ResourceURI.",
                        max_length=64,
                        null=True,
                    ),
                ),
                (
                    "last_modified_date",
                    models.DateTimeField(
                        blank=True,
                        db_index=True,
                        help_text="Timestamp set to the last modified date of the remote resource represented by this URI such as the modified date of a file, the lastmod value on a sitemap or the modified date returned by an HTTP resource.",
                        null=True,
                    ),
                ),
                (
                    "service",
                    models.CharField(
                        blank=True,
                        help_text="The name of the service running where the error occured.",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(
                        blank=True,
                        db_index=True,
                        help_text="Timestamp set to the date of when this error occured.",
                        null=True,
                    ),
                ),
                (
                    "error_message",
                    models.TextField(
                        blank=True,
                        help_text="The message associated with this error",
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Processing Error",
            },
        ),
    ]