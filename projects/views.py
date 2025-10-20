from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project

from .serializers.common import ProjectSerializer

from rest_framework.exceptions import NotFound, PermissionDenied

# * Path: /projects

class ProjectsListView(APIView):

    def get(self, request):
        projects = Project.objects.all()
        serialized_projects = ProjectSerializer(projects, many=True)
        return Response(serialized_projects.data)




# * Path: /projects/<int:pk>

class ProjectDetailView(APIView):

    # 404
    def get_project(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist as e:
            print(e)
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
        return Response(serialized_project.validated_data)
    
    # Delete
    def delete(self, request, pk):
        project = self.get_project(pk)    
        project.delete()
        return Response(status=204)