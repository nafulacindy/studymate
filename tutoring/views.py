from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets, permissions
from .models import TutoringSession
from .serializers import TutoringSessionSerializer


class TutoringSessionViewSet(viewsets.ModelViewSet):
    queryset = TutoringSession.objects.all().order_by('-date_time')
    serializer_class = TutoringSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.instance.tutor != self.request.user and serializer.instance.student != self.request.user:
            raise PermissionDenied("You can only update sessions you are part of.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.tutor != self.request.user and instance.student != self.request.user:
            raise PermissionDenied("You can only cancel sessions you are part of.")
        instance.delete()

