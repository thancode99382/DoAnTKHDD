from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('detail-job/<slug:slug>/', views.DetailJobView.as_view(), name='detail-job'),
    path('create-company/', views.create_company, name='create-company'),
    path('filter-job-by-keyword/<str:keyword>/', views.filter_job_by_keyword, name='filter-job-by-keyword'),
]
