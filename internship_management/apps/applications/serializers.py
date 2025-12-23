from rest_framework import serializers
from .models import Application


class ApplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ("id", "internship", "resume")

    def validate(self, attrs):
        user = self.context["request"].user
        internship = attrs["internship"]

        if Application.objects.filter(
            internship=internship,
            student=user
        ).exists():
            raise serializers.ValidationError(
                "You have already applied to this internship."
            )

        return attrs

    def create(self, validated_data):
        user = self.context["request"].user
        return Application.objects.create(
            student=user,
            **validated_data
        )


