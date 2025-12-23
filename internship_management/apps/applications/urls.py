from django.urls import path
from .views import (
    MyApplicationsView,
    UpdateApplicationStatusView,
)

urlpatterns = [
    path("my/", MyApplicationsView.as_view(), name="my-applications"),
    path("<int:pk>/status/", UpdateApplicationStatusView.as_view(), name="update-status"),
]
