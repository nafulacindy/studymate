from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class TutoringSession(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tutor_sessions')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_sessions')
    subject = models.CharField(max_length=120)
    date_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f'{self.subject} - {self.tutor} with {self.student} on {self.date_time:%Y-%m-%d %H:%M}'

# Create your models here.
