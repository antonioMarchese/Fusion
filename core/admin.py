from django.contrib import admin
from .models import Teammate, Role, Service

@admin.register(Role)
class AdminRole(admin.ModelAdmin):
    list_display = ['role', 'active', 'created_at', 'updated_at']

@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display = ['name', 'description', 'logo', 'active', 'created_at', 'updated_at']

@admin.register(Teammate)
class AdminTeammate(admin.ModelAdmin):
    list_display = ['name', 'role', 'created_at', 'updated_at', 'active']