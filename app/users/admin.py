from django.contrib import admin

from users.models import *


# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'phone', 'created_at', 'full_name',)
    search_fields = ('user__username', 'full_name', 'phone')
    list_filter = ('created_at', )


admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Employer)
