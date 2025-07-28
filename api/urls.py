from django.urls import path, include
from django.views.generic import RedirectView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("customers/", include("customers.urls")),
    path("orders/", include("orders.urls")),
    path("products/", include("products.urls")),
    
    # API schema generation
    # Optional: Use drf-spectacular for OpenAPI schema generation

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    
    path("", RedirectView.as_view(url="docs/", permanent=False)),
]