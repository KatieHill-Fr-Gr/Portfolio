from django.urls import path
from technologies.views import TechnologiesListView

urlpatterns = [
    path('', TechnologiesListView.as_view()),
]