from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import ManagerModelSerializer
from .models import Manager

class ManagerModelViewSet(ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerModelSerializer



