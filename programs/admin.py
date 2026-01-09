from django.contrib import admin
from .models import Program, Enrollment

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'coordinator', 'start_date', 'capacity')
    search_fields = ('title', 'description')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'program', 'status', 'enrolled_at')
    list_filter = ('status', 'program')
