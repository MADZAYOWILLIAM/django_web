from django.contrib import admin

from .models import Service, ServiceRequest


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'status', 'created_at')
    list_filter = ('status', 'service')
    search_fields = ('user__username', 'service__name', 'message')
