from rest_framework.permissions import BasePermission


class CanViewApplication(BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.role == "ADMIN":
            return True

        if user.role == "RECRUITER":
            return obj.internship.recruiter == user

        if user.role == "STUDENT":
            return obj.student == user

        return False
