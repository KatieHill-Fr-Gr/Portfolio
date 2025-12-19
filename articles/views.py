from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article

from .serializers.common import ArticleSerializer
from users.serializers.common import ContributorSerializer

from rest_framework.exceptions import NotFound


class ArticlesListView(APIView):

    def get(self, request):
        articles = Article.objects.prefetch_related('images').all()
        serialized_articles = ArticleSerializer(articles, many=True)
        return Response(serialized_articles.data)
    
    def post(self, request):
        serialized_articles = ArticleSerializer(data=request.data) 
        serialized_articles.is_valid(raise_exception=True) 
        serialized_articles.save()
        return Response(serialized_articles.data) 
    

class ArticleDetailView(APIView):

    def get_article(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise NotFound('Article does not exist.')  
        
    def get(self, request, pk):
        article = self.get_article(pk)
        serialized_article = ArticleSerializer(article)
        return Response(serialized_article.data)       
    
    def put(self, request, pk):
        article = self.get_article(pk)
        serialized_article = ArticleSerializer(article, data=request.data, partial=True)
        serialized_article.is_valid(raise_exception=True)
        serialized_article.save()
        return Response(ArticleSerializer(article).data)
     
    def delete(self, request, pk):
        article = self.get_article(pk)    
        article.delete()
        return Response(status=204)