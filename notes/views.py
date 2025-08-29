from rest_framework import viewsets, permissions, filters
from rest_framework.exceptions import PermissionDenied
from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

    def get_queryset(self):
        return Note.objects.all().order_by('-created_at')

    def perform_update(self, serializer):
        if serializer.instance.uploaded_by != self.request.user:
            raise PermissionDenied("You cannot edit someone else’s note.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.uploaded_by != self.request.user:
            raise PermissionDenied("You cannot delete someone else’s note.")
        instance.delete()




