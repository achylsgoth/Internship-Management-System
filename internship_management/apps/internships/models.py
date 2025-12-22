from django.db import models
from apps.accounts.models import User


class Internship(models.Model):

    recruiter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="internships"
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    stipend = models.PositiveIntegerField(null=True, blank=True)
    duration = models.CharField(max_length=100)
    deadline = models.DateField()

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
