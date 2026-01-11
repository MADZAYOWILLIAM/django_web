from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Profile.objects.create(user=user)
        return user
