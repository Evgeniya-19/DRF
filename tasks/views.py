from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import ProjectModelSerializer, TaskModelSerializer
from .models import Project, Task

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

class TaskModelViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer