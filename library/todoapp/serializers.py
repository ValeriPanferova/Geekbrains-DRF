from rest_framework.serializers import HyperlinkedRelatedField, ModelSerializer, StringRelatedField

from .models import TODO, Project


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class TODOModelSerializer(ModelSerializer):
    project = ProjectModelSerializer()

    class Meta:
        model = TODO
        fields = "__all__"


class TODOModelSerializerBase(ModelSerializer):
    class Meta:
        model = TODO
        fields = "__all__"
