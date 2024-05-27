from django.contrib import admin


from .models import *

# Register your models here.
admin.site.register(CV)
admin.site.register(Interview)
admin.site.register(Feedback)
admin.site.register(Application)