from django.urls import path, include
from django.views.generic import RedirectView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from customers.views import CustomUserViewSet

router = DefaultRouter()
router.register(r'customers', CustomUserViewSet)



urlpatterns = [
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
] + router.urls