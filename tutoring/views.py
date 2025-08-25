from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import TutoringSession
from .serializers import TutoringSessionSerializer

class TutoringSessionViewSet(viewsets.ModelViewSet):
    queryset = TutoringSession.objects.all().order_by('-date_time')
    serializer_class = TutoringSessionSerializer
    permission_classes = [permissions.IsAuthenticated]
