from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('register-employer/', views.RegisterEmployer.as_view(), name='register-employer'),
]
