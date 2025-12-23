from rest_framework import serializers
from .models import Internship


class InternshipSerializer(serializers.ModelSerializer):
    recruiter = serializers.ReadOnlyField(source="recruiter.email")

    class Meta:
        model = Internship
        fields = (
            "id",
            "recruiter",
            "title",
            "description",
            "location",
            "stipend",
            "duration",
            "deadline",
            "is_active",
            "created_at",
        )
