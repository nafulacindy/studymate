from django.db import models
from django.conf import settings

class Note(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='notes/')   # <--- NOT subject
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
