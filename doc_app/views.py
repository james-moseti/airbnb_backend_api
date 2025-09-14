from rest_framework import viewsets
from .models import PropertyListing
from .serializers import PropertyListingSerializer

class PropertyListingViewSet(viewsets.ModelViewSet):
    queryset = PropertyListing.objects.all()
    serializer_class = PropertyListingSerializer