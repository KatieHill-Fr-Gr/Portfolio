from django.urls import path
from projects.views import ProjectsListView, ProjectDetailView, ProjectUsersListView

urlpatterns = [
    path('', ProjectsListView.as_view()),
    path('<int:pk>/', ProjectDetailView.as_view()),
    path('<int:pk>/users/', ProjectUsersListView.as_view(), name='project-users-list'),
]