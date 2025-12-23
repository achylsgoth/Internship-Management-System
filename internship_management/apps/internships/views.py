from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Internship
from .serializers import InternshipSerializer
from apps.accounts.permissions import IsRecruiter
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .permissions import IsOwnerRecruiter


class InternshipListCreateView(ListCreateAPIView):
    queryset = Internship.objects.filter(is_active=True)
    serializer_class = InternshipSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(recruiter=self.request.user)

class InternshipDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer
    permission_classes = [IsAuthenticated, IsOwnerRecruiter]