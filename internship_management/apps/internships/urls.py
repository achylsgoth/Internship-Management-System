from django.urls import path
from .views import (
    InternshipListCreateView,
    InternshipDetailView,
)
from apps.applications.views import (
    InternshipApplicationsView,
    ApplyInternshipView,
)

urlpatterns = [
    path("", InternshipListCreateView.as_view(), name="internship-list"),
    path("<int:pk>/", InternshipDetailView.as_view(), name="internship-detail"),

    # nested application routes
    path("<int:internship_id>/apply/", ApplyInternshipView.as_view(), name="apply"),
    path(
        "<int:internship_id>/applications/",
        InternshipApplicationsView.as_view(),
        name="internship-applications",
    ),
]
