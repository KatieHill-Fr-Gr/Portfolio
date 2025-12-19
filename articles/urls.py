from django.urls import path
from articles.views import ArticlesListView, ArticleDetailView

urlpatterns = [
    path('', ArticlesListView.as_view()),
    path('<int:pk>/', ArticleDetailView.as_view()),
]