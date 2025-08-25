from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class StudyGroup(models.Model):
    name = models.CharField(max_length=120)
    subject = models.CharField(max_length=120)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='groups_created')
    members = models.ManyToManyField(User, through='StudyGroupMembership', related_name='study_groups')

    def __str__(self):
        return f'{self.name} ({self.subject})'

class StudyGroupMembership(models.Model):
    study_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('study_group', 'user')

class GroupMessage(models.Model):
    group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# Create your models here.
