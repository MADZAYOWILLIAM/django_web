from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', _('Admin')
        YOUTH_LEADER = 'LEADER', _('Youth Leader')
        MENTOR = 'MENTOR', _('Mentor')
        YOUTH_MEMBER = 'MEMBER', _('Youth Member')
        VOLUNTEER = 'VOLUNTEER', _('Volunteer')
        GUEST = 'GUEST', _('Guest')

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.YOUTH_MEMBER)
    email = models.EmailField(unique=True)

    def is_youth_member(self):
        return self.role == self.Role.YOUTH_MEMBER
    
    def is_mentor(self):
        return self.role == self.Role.MENTOR
    
    def is_admin(self):
        return self.role == self.Role.ADMIN

    def  is_volunteer(self):
        return self.role == self.Role.VOLUNTEER
    
    def is_guest(self):
        return self.role == self.Role.GUEST

    def is_youth_leader(self):
        return self.role == self.Role.YOUTH_LEADER
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    
    # Specific fields for Youth
    date_of_birth = models.DateField(null=True, blank=True)
    skills = models.TextField(blank=True, help_text="Comma separated skills")
    interests = models.TextField(blank=True, help_text="Comma separated interests")
    
    # Specific fields for Mentor
    expertise = models.TextField(blank=True, help_text="Area of expertise")
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
