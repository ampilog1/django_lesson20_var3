from .models import Region
from .serializers import RegionSerializer
from rest_framework import viewsets


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
