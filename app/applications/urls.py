from django.urls import path

from . import views

app_name = "applications"

urlpatterns = [
    path("post-recruitment/", views.post_recruitment, name="post-recruitment"),
    path(
        "company/<slug:slug>/", views.CompanyDetailView.as_view(), name="company-detail"
    ),
    path("submit-cv/", views.SubmitCV.as_view(), name="submit-cv"),
    path("view-applicant/", views.view_applicant_cv, name="view-applicant-cv"),
    path("cv-detail/<int:pk>/", views.cv_detail, name="cv-detail"),
    path("reject-cv/<int:cv_id>/", views.reject_cv, name="reject-cv"),
]
