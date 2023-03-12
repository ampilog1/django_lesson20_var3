from django.urls import path, include
from .models import Region, Skills
from rest_framework import routers, serializers, viewsets


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class SkillsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'
