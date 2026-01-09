from django.contrib import admin
from .models import Event, Attendance

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'date', 'organizer')
    list_filter = ('event_type', 'date')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'status', 'check_in_time')
    list_filter = ('status', 'event')
