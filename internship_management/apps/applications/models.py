from django.db import models
from apps.accounts.models import User
from apps.internships.models import Internship


class Application(models.Model):

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        ACCEPTED = "ACCEPTED", "Accepted"
        REJECTED = "REJECTED", "Rejected"

    internship = models.ForeignKey(
        Internship,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    resume = models.FileField(upload_to="resumes/")
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("internship", "student")
        ordering = ["-applied_at"]

    def __str__(self):
        return f"{self.student.email} → {self.internship.title}"
