# Generated by Django 4.1.9 on 2023-11-28 20:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("file_versions", "0005_rename_file_filedata_cas_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="filedata",
            name="cas_location",
            field=models.CharField(max_length=100),
        ),
    ]