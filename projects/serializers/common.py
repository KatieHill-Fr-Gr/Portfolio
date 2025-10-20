from rest_framework.serializers import ModelSerializer
from ..models import Project

class ProjectSerializer(ModelSerializer):
     class Meta:
            model = Project
            fields = ['name', 'description', 'contributor', 'technologies', 'data_completed', 'is_public']

