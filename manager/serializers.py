from rest_framework.serializers import ModelSerializer


from .models import Manager


class ManagerModelSerializer(ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'
