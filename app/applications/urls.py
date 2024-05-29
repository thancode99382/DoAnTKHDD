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
    path("accept-cv/<int:cv_id>/", views.accept_cv, name="accept-cv"),
    path("search/", views.search_job, name="search"),
    path("search-keyword/", views.search_job_keyword, name="search-keyword"),
    path("company-list/", views.CompanyListView.as_view(), name="company-list"),

]
