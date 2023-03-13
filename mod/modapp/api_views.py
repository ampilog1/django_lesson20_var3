from .models import Region, Skills
from .serializers import RegionSerializer, SkillsSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated, BasePermission
from .permissions import ReadOnly


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class SkillsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
