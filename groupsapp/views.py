from django.core.exceptions import PermissionDenied
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import StudyGroup, GroupMessage
from .serializers import StudyGroupSerializer, GroupMessageSerializer
from django_filters.rest_framework import DjangoFilterBackend


class StudyGroupViewSet(viewsets.ModelViewSet):
    """
    API for study groups:
    - Anyone can view groups
    - Only authenticated users can create
    - Only creator can delete
    - Join/Leave actions for members
    """
    queryset = StudyGroup.objects.all().order_by('name')
    serializer_class = StudyGroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['subject', 'created_by']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_destroy(self, instance):
        if instance.created_by != self.request.user:
            raise PermissionDenied("Only the creator can delete this group.")
        instance.delete()

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def join(self, request, pk=None):
        group = self.get_object()
        user = request.user
        if group.members.filter(id=user.id).exists():
            return Response({'detail': 'Already a member'}, status=status.HTTP_400_BAD_REQUEST)
        group.members.add(user)
        return Response({'detail': 'Joined group successfully'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def leave(self, request, pk=None):
        group = self.get_object()
        user = request.user
        if not group.members.filter(id=user.id).exists():
            return Response({'detail': 'Not a member'}, status=status.HTTP_400_BAD_REQUEST)
        group.members.remove(user)
        return Response({'detail': 'Left group successfully'}, status=status.HTTP_200_OK)


class GroupMessageViewSet(viewsets.ModelViewSet):
    """
    API for group messages:
    - Only members of a group can post or view its messages
    """
    queryset = GroupMessage.objects.all().order_by('-timestamp')
    serializer_class = GroupMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        group = serializer.validated_data['group']
        if not group.members.filter(id=self.request.user.id).exists():
            raise PermissionDenied("You must be a group member to post messages.")
        serializer.save(sender=self.request.user)

    def get_queryset(self):
        # Only return messages from groups the user is a member of
        return GroupMessage.objects.filter(group__members=self.request.user)
