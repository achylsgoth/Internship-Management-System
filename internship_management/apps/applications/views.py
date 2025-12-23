from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ApplySerializer
from apps.accounts.permissions import IsStudent


class ApplyInternshipView(CreateAPIView):
    serializer_class = ApplySerializer
    permission_classes = [IsAuthenticated, IsStudent]

from rest_framework.generics import ListAPIView
from .models import Application


class MyApplicationsView(ListAPIView):
    serializer_class = ApplySerializer
    permission_classes = [IsAuthenticated, IsStudent]

    def get_queryset(self):
        return Application.objects.filter(student=self.request.user)


from apps.accounts.permissions import IsRecruiter


class InternshipApplicationsView(ListAPIView):
    serializer_class = ApplySerializer
    permission_classes = [IsAuthenticated, IsRecruiter]

    def get_queryset(self):
        internship_id = self.kwargs["internship_id"]
        return Application.objects.filter(
            internship_id=internship_id,
            internship__recruiter=self.request.user
        )

from rest_framework.generics import UpdateAPIView
from .permissions import CanViewApplication
from .serializers import ApplicationStatusSerializer


class UpdateApplicationStatusView(UpdateAPIView):
    serializer_class = ApplicationStatusSerializer
    permission_classes = [IsAuthenticated, CanViewApplication]
    queryset = Application.objects.all()
