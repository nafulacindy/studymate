from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import StudyGroup, StudyGroupMembership, GroupMessage
from .serializers import StudyGroupSerializer, StudyGroupMembershipSerializer, GroupMessageSerializer

class StudyGroupViewSet(viewsets.ModelViewSet):
    queryset = StudyGroup.objects.all().order_by('name')
    serializer_class = StudyGroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StudyGroupMembershipViewSet(viewsets.ModelViewSet):
    queryset = StudyGroupMembership.objects.all()
    serializer_class = StudyGroupMembershipSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupMessageViewSet(viewsets.ModelViewSet):
    queryset = GroupMessage.objects.all().order_by('-timestamp')
    serializer_class = GroupMessageSerializer
    permission_classes = [permissions.IsAuthenticated]
