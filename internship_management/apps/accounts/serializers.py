from rest_framework import serializers
from .models import User
from rest_framework import serializers
from apps.applications.models import Application

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    class Meta:
        model = User
        fields = ("email", "full_name", "password", "role")

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(
            password=password,
            **validated_data
        )
        return user

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


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "role",
            "created_at",
        )