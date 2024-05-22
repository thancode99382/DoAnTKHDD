from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('company/', views.Company.as_view(), name='company'),
]
