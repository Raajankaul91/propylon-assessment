# Generated by Django 4.1.9 on 2023-11-28 20:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("file_versions", "0006_alter_filedata_cas_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="filedata",
            name="cas_location",
            field=models.CharField(default="000/000/000", max_length=100),
        ),
    ]
