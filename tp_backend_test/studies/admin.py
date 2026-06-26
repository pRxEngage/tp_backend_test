from django.contrib import admin

from .models import Study
from .models import UploadTask


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = [
        "nct_id",
        "brief_title",
        "overall_status",
        "study_type",
        "updated_at",
    ]
    search_fields = ["nct_id", "brief_title", "official_title", "overall_status"]
    list_filter = ["overall_status", "study_type"]
    readonly_fields = ["created_at", "updated_at"]
    ordering = ["nct_id"]


@admin.register(UploadTask)
class UploadTaskAdmin(admin.ModelAdmin):
    list_display = [
        "source_file",
        "created_at",
        "updated_at",
    ]
    readonly_fields = ["created_at", "updated_at"]
