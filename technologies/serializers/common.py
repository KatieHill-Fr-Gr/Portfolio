from rest_framework.serializers import ModelSerializer
from ..models import Technology

class TechnologySerializer(ModelSerializer):
     class Meta:
            model = Technology
            fields = ['name', 'icon']