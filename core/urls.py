from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("", include("customers.urls")),
    path("", include("orders.urls")),
    path("", include("products.urls")),
    path("", RedirectView.as_view(url="/api/docs/", permanent=False)),
]
