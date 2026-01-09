from django.db import models
from django.conf import settings

class Event(models.Model):
    TYPE_CHOICES = [
        ('PHYSICAL', 'Physical'),
        ('VIRTUAL', 'Virtual'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='PHYSICAL')
    date = models.DateTimeField()
    location = models.CharField(max_length=255, help_text="Physical location or Virtual meeting link")
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='organized_events')
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('REGISTERED', 'Registered'),
        ('PRESENT', 'Present'),
        ('ABSENT', 'Absent'),
        ('EXCUSED', 'Excused'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='event_attendance')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendance')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='REGISTERED')
    registration_date = models.DateTimeField(auto_now_add=True)
    check_in_time = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        unique_together = ('user', 'event')
