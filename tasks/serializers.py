from rest_framework.serializers import ModelSerializer


from .models import Project, Task


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TaskModelSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'