from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('detail-job/<slug:slug>/', views.DetailJobView.as_view(), name='detail-job'),
    path('create-company/', views.create_company, name='create-company'),
]
