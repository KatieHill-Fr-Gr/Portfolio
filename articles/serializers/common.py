from rest_framework.serializers import ModelSerializer
from users.serializers.common import ContributorSerializer
from technologies.serializers.common import TechnologySerializer
from ..models import Article, ArticleImage

class ArticleImageSerializer(ModelSerializer):
     class Meta:
            model = ArticleImage
            fields = ['image_url', 'caption', 'is_primary', 'uploaded_at']

class ArticleSerializer(ModelSerializer):
     contributors = ContributorSerializer(many=True, read_only=True)
     images = ArticleImageSerializer(many=True, read_only=True) 

     class Meta:
            model = Project
            fields = ['id', 'title', 'subtitle', 'summary', 'body', 'contributors','date_completed', 'is_public', 'images']

