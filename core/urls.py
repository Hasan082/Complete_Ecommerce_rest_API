from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("", RedirectView.as_view(url="/api/docs/", permanent=False)),
]
