from django.urls import path
from users import views


app_name = "users"

urlpatterns = [
    path("login/", views.Login.as_view(), name="login"),
    path("register/", views.Register.as_view(), name="register"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.RegisterCandidate.as_view(), name="profile"),
    path(
        "register-employer/<int:pk>/",
        views.RegisterEmployer.as_view(),
        name="register-employer",
    ),
    path("update-profile/", views.update_profile, name="profile-update"),
]
