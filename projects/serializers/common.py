from rest_framework.serializers import ModelSerializer
from users.serializers.common import ContributorSerializer
from technologies.serializers.common import TechnologySerializer
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
     contributors = ContributorSerializer(many=True, read_only=True)
     images = ProjectImageSerializer(many=True, read_only=True) 
     links = ProjectLinkSerializer(many=True, read_only=True)
     technologies = TechnologySerializer(many=True, read_only=True)

     class Meta:
            model = Project
            fields = ['id', 'name', 'description1', 'description2', 'description3', 'subtitle', 'summary', 'contributors', 'technologies', 'date_completed', 'is_public', 'images', 'links']

