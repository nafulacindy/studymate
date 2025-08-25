from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Note(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=120)
    file = models.CharField(max_length=255)  # keep simple path/string for now
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
