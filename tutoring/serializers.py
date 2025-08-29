from rest_framework import serializers
from .models import TutoringSession
from django.utils import timezone

class TutoringSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutoringSession
        fields = '__all__'

    def validate_date_time(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError("Session must be scheduled in the future.")
        return value
