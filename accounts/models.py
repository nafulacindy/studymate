from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    # AbstractUser already has: username, email, password, first_name, last_name
    subjects_can_tutor = models.TextField(blank=True, default='')
    subjects_need_help = models.TextField(blank=True, default='')
    available_times = models.TextField(blank=True, default='') 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username or self.email




