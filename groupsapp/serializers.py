from rest_framework import serializers
from .models import StudyGroup, StudyGroupMembership, GroupMessage

class StudyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = ['id', 'name', 'subject', 'created_by', 'members']
        read_only_fields = ['id']

class StudyGroupMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGroupMembership
        fields = ['id', 'study_group', 'user', 'joined_at']
        read_only_fields = ['id', 'joined_at']

class GroupMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMessage
        fields = ['id', 'group', 'sender', 'content', 'timestamp']
        read_only_fields = ['id', 'timestamp']
