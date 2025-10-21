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
        projects = Project.objects.prefetch_related('images', 'links').all() # Reduce the number of calls to the api
        serialized_projects = ProjectSerializer(projects, many=True)
        return Response(serialized_projects.data)
    
    def post(self, request):
        serialized_projects = ProjectSerializer(data=request.data) # deserialize request data
        serialized_projects.is_valid(raise_exception=True) # validate request data
        serialized_projects.save() # save it
        return Response(serialized_projects.data) # return the data
        
        
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
        return Response(ProjectSerializer(project).data) # Return the full project object including image and links
    
    # Delete
    def delete(self, request, pk):
        project = self.get_project(pk)    
        project.delete()
        return Response(status=204)
    
# * Path: /projects/<int:pk>/contributors

class ProjectContributorsView(APIView):
    serializer_class = ContributorSerializer
    
    # def get_queryset(self):
    #     project_id = self.kwargs.get('pk')
    #     project = Project.objects.select_related('contributed_projects').filter(pk=project_id).first()
    #     if project:
    #         return User.objects.filter(team=project.team)
    #     return User.objects.none()