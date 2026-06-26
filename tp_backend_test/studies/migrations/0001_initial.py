# Generated for the trialport backend assessment scaffold.

import django.utils.timezone
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Study",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(default=django.utils.timezone.now, editable=False),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("nct_id", models.CharField(db_index=True, max_length=11, unique=True)),
                ("brief_title", models.TextField(blank=True)),
                ("official_title", models.TextField(blank=True)),
                ("overall_status", models.CharField(blank=True, max_length=64)),
                ("conditions", models.JSONField(blank=True, default=list)),
                ("study_type", models.CharField(blank=True, max_length=64)),
                ("brief_summary", models.TextField(blank=True)),
                ("sponsor_primary_key", models.CharField(blank=True, max_length=255)),
            ],
            options={
                "ordering": ["nct_id"],
            },
        ),
        migrations.CreateModel(
            name="UploadTask",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(default=django.utils.timezone.now, editable=False),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("source_file", models.FileField(upload_to="study_uploads/")),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
