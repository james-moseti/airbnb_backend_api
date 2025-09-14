from django.urls import path, include
from .views import PropertyListingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"properties", PropertyListingViewSet, basename="propertylisting")

urlpatterns = [
    path("", include(router.urls)),
]