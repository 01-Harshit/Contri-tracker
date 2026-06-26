from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Project, Task, Group
from .serializers import ProjectSerializer, TaskSerializer, GroupSerializer
from django.contrib.auth.models import User

#all project list
class ProjectListAPI(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Project.objects.all()

    def perform_create(self, serializer):
        # Pehla user assign kar do temporarily
        teacher = User.objects.first()
        serializer.save(teacher=teacher)
        
# single project list
class ProjectDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Project.objects.all()

class TaskListAPI(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Task.objects.all()