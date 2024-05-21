from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('detailjob/', views.DetailJob.as_view(), name='detailjob'),
]
