from __future__ import annotations

from django.db import models
from django.utils import timezone


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Study(TimestampedModel):
    nct_id = models.CharField(max_length=11, unique=True, db_index=True)
    brief_title = models.TextField(blank=True)
    official_title = models.TextField(blank=True)
    overall_status = models.CharField(max_length=64, blank=True)
    conditions = models.JSONField(default=list, blank=True)
    study_type = models.CharField(max_length=64, blank=True)
    brief_summary = models.TextField(blank=True)
    sponsor_primary_key = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["nct_id"]

    def __str__(self) -> str:
        return self.nct_id

    def save(self, *args, **kwargs):
        self.nct_id = self.nct_id.upper()
        super().save(*args, **kwargs)


class UploadTask(TimestampedModel):
    source_file = models.FileField(upload_to="study_uploads/")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.source_file.name or f"Upload task {self.pk}"
