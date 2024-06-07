from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import *


# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'is_employer', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active', 'is_employer']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Additional info', {'fields': ('is_employer',)}),  # custom fields
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_employer', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)


class CandidateAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'phone', 'created_at', 'full_name',)
    search_fields = ('user__username', 'full_name', 'phone')
    list_filter = ('created_at',)


admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Employer)
admin.site.register(Location)
admin.site.register(CustomUser, CustomUserAdmin)
