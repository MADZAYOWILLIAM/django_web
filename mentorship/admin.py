from django.contrib import admin
from .models import MentorshipSession

@admin.register(MentorshipSession)
class MentorshipSessionAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'mentee', 'scheduled_at', 'status')
    list_filter = ('status', 'scheduled_at')
