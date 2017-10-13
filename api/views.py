from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .serializers import UserSerializer, GroupSerializer, ClientSerializer, ProjectSerializer
from rest_framework import viewsets

from tracker.models import Client, Project


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = get_user_model().objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    search_fields = ('name', 'client')
    ordering_fields = ('name',)
    ordering = ('name',)


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited
    """
    queryset = Project.objects.all().order_by('name')
    serializer_class = ProjectSerializer
    filter_fields = ('client',)
    search_fields = ('name', 'client__name')
    ordering_fields = ('name', 'client__name', 'created')
    ordering = ('-created',)
