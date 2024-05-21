from django.contrib import admin
from django.utils.text import slugify

from .models import *


class HurryJobInline(admin.TabularInline):
    model = HurryJob
    can_delete = False
    verbose_name_plural = 'Hurry Job'


class JobAdmin(admin.ModelAdmin):
    inlines = [
        HurryJobInline,
    ]

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)


class CompanyAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)


# Register your models here.
admin.site.register(Company, CompanyAdmin)
admin.site.register(Keyword)
admin.site.register(Job, JobAdmin)
admin.site.register(HurryJob)
admin.site.register(TopCompany)
admin.site.register(JobCategory)
