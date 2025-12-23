from django.contrib import admin
from .models import Internship


@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "recruiter",
        "location",
        "stipend",
        "deadline",
        "is_active",
        "created_at",
    )
    list_filter = ("location", "is_active", "deadline")
    search_fields = ("title", "description")
