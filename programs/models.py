from django.db import models
from django.conf import settings

class Program(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    coordinator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='coordinated_programs')
    start_date = models.DateField()
    end_date = models.DateField()
    capacity = models.PositiveIntegerField(default=50)
    image = models.ImageField(upload_to='program_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('COMPLETED', 'Completed'),
        ('DROPPED', 'Dropped'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrollments')
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='enrollments')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    enrolled_at = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateField(null=True, blank=True)
    certificate_issued = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'program')
