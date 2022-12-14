# Generated by Django 4.1.2 on 2022-10-26 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("packagedb", "0050_alter_resource_extra_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="package",
            name="api_data_url",
            field=models.CharField(
                blank=True,
                help_text="API URL to obtain structured data for this package such as the URL to a JSON or XML api its package repository.",
                max_length=1024,
                null=True,
                verbose_name="API data URL",
            ),
        ),
        migrations.AddField(
            model_name="package",
            name="datasource_id",
            field=models.CharField(
                blank=True,
                help_text="The identifier for the datafile handler used to obtain this package.",
                max_length=64,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="package",
            name="file_references",
            field=models.JSONField(
                blank=True,
                default=list,
                help_text="List of file paths and details for files referenced in a package manifest. These may not actually exist on the filesystem. The exact semantics and base of these paths is specific to a package type or datafile format.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="package",
            name="manifest_path",
            field=models.CharField(
                blank=True,
                help_text="A relative path to the manifest file if any, such as a Maven .pom or a npm package.json.",
                max_length=1024,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="package",
            name="repository_download_url",
            field=models.CharField(
                blank=True,
                help_text="Download URL to download the actual archive of code of this package in its package repository. This may be different from the actual download URL.",
                max_length=1024,
                null=True,
                verbose_name="Repository download URL",
            ),
        ),
        migrations.AddField(
            model_name="package",
            name="repository_homepage_url",
            field=models.CharField(
                blank=True,
                help_text="URL to the page for this package in its package repository. This is typically different from the package homepage URL proper.",
                max_length=1024,
                null=True,
                verbose_name="Repository homepage URL",
            ),
        ),
        migrations.AlterField(
            model_name="package",
            name="bug_tracking_url",
            field=models.CharField(
                blank=True,
                help_text="URL to the issue or bug tracker for this package.",
                max_length=1024,
                null=True,
                verbose_name="Bug tracking URL",
            ),
        ),
        migrations.AlterField(
            model_name="package",
            name="code_view_url",
            field=models.CharField(
                blank=True,
                help_text="a URL where the code can be browsed online.",
                max_length=1024,
                null=True,
                verbose_name="Code view URL",
            ),
        ),
        migrations.AlterField(
            model_name="package",
            name="declared_license",
            field=models.TextField(
                blank=True,
                help_text="The declared license mention or tag or text as found in a package manifest.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="package",
            name="download_url",
            field=models.CharField(
                db_index=True,
                help_text="A direct download URL.",
                max_length=2048,
                unique=True,
                verbose_name="Download URL",
            ),
        ),
        migrations.AlterField(
            model_name="package",
            name="extra_data",
            field=models.JSONField(
                blank=True,
                default=dict,
                help_text="Optional mapping of extra data key/values.",
            ),
        ),
        migrations.AlterField(
            model_name="package",
            name="homepage_url",
            field=models.CharField(
                blank=True,
                help_text="URL to the homepage for this package.",
                max_length=1024,
                null=True,
                verbose_name="Homepage URL",
            ),
        ),
        migrations.AlterField(
            model_name="package",
            name="license_expression",
            field=models.TextField(
                blank=True,
                help_text="The normalized license expression for this package as derived from its declared license.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="package",
            name="md5",
            field=models.CharField(
                blank=True,
                help_text="MD5 checksum hex-encoded, as in md5sum.",
                max_length=32,
                null=True,
                verbose_name="MD5",
            ),
        ),
        migrations.AlterField(
            model_name="package",
            name="primary_language",
            field=models.CharField(
                blank=True,
                help_text="Primary programming language.",
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="package",
            name="sha1",
            field=models.CharField(
                blank=True,
                help_text="SHA1 checksum hex-encoded, as in sha1sum.",
                max_length=40,
                null=True,
                verbose_name="SHA1",
            ),
        ),
        migrations.AlterField(
            model_name="package",
            name="sha256",
            field=models.CharField(
                blank=True,
                help_text="SHA256 checksum hex-encoded, as in sha256sum.",
                max_length=64,
                null=True,
                verbose_name="SHA256",
            ),
        ),
        migrations.AlterField(
            model_name="package",
            name="sha512",
            field=models.CharField(
                blank=True,
                help_text="SHA512 checksum hex-encoded, as in sha512sum.",
                max_length=128,
                null=True,
                verbose_name="SHA512",
            ),
        ),
        migrations.AlterField(
            model_name="package",
            name="vcs_url",
            field=models.CharField(
                blank=True,
                help_text='A URL to the VCS repository in the SPDX form of: "git", "svn", "hg", "bzr", "cvs", https://github.com/nexb/scancode-toolkit.git@405aaa4b3 See SPDX specification "Package Download Location" at https://spdx.org/spdx-specification-21-web-version#h.49x2ik5',
                max_length=1024,
                null=True,
                verbose_name="VCS URL",
            ),
        ),
    ]
