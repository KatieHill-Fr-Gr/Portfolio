from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project

from .serializers.common import ProjectSerializer
from users.serializers.common import ContributorSerializer

from rest_framework.exceptions import NotFound

# * Path: /projects

class ProjectsListView(APIView):

    def get(self, request):
        projects = Project.objects.prefetch_related('images', 'links').all() 
        serialized_projects = ProjectSerializer(projects, many=True)
        return Response(serialized_projects.data)
    
    def post(self, request):
        serialized_projects = ProjectSerializer(data=request.data) 
        serialized_projects.is_valid(raise_exception=True) 
        serialized_projects.save()
        return Response(serialized_projects.data)
    
    
class ProjectUsersListView(APIView):
    def get (self, request, pk):
        try: 
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response({"error": "Project not found"}, status=404)
        users = project.contributors.all()
        serializer = ContributorSerializer(users, many=True)
        return Response(serializer.data)
        
        
# * Path: /projects/<int:pk>

class ProjectDetailView(APIView):

    # 404
    def get_project(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise NotFound('Project does not exist.')  
        
    # Show
    def get(self, request, pk):
        project = self.get_project(pk)
        serialized_project = ProjectSerializer(project)
        return Response(serialized_project.data)
        
    
    # Update
    def put(self, request, pk):
        project = self.get_project(pk)
        serialized_project = ProjectSerializer(project, data=request.data, partial=True)
        serialized_project.is_valid(raise_exception=True)
        serialized_project.save()
        return Response(ProjectSerializer(project).data)
    
    # Delete
    def delete(self, request, pk):
        project = self.get_project(pk)    
        project.delete()
        return Response(status=204)
    