from rest_framework.serializers import ModelSerializer
from ..models import Project, ProjectImage, ProjectLink

class ProjectImageSerializer(ModelSerializer):
     class Meta:
            model = ProjectImage
            fields = ['image_url', 'caption', 'is_primary', 'uploaded_at']

class ProjectLinkSerializer(ModelSerializer):
     class Meta:
            model = ProjectLink
            fields = ['url', 'link_type', 'label']

class ProjectSerializer(ModelSerializer):
     images = ProjectImageSerializer(many=True, read_only=True) 
     links = ProjectLinkSerializer(many=True, read_only=True)

     class Meta:
            model = Project
            fields = ['name', 'description', 'contributor', 'technologies', 'date_completed', 'is_public', 'images', 'links']

