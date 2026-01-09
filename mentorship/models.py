from django.db import models
from django.conf import settings

class MentorshipSession(models.Model):
    mentor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mentorship_sessions_as_mentor')
    mentee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mentorship_sessions_as_mentee')
    scheduled_at = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(default=60)
    notes = models.TextField(blank=True)
    status_choices = [
        ('SCHEDULED', 'Scheduled'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='SCHEDULED')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Session: {self.mentor} - {self.mentee} on {self.scheduled_at}"
