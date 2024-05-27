from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import generic

from applications.forms import CVForm
from applications.models import CV
from jobs.models import Company, Job
from users.forms import RecruitmentForm


class CompanyDetailView(generic.DetailView):
    template_name = "applications/company.html"
    model = Company
    context_object_name = "company"
    slug_field = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Detail Job"
        # Get all the recruitments belongs to that company
        context["recruitment"] = Job.objects.filter(company=self.object)
        return context


# Create your views here.
@login_required
def post_recruitment(request):
    if request.method == "POST":
        form = RecruitmentForm(request.POST, user=request.user)
        if form.is_valid():
            recruitment = form.save(commit=False)
            recruitment.slug = slugify(recruitment.title)
            recruitment.save()
            return redirect("core:home")
    else:
        form = RecruitmentForm(user=request.user)
    return render(request, "applications/post_recruitment.html", {"form": form})


class SubmitCV(generic.CreateView):
    form_class = CVForm
    success_url = reverse_lazy("core:home")

    # template_name = "applications/submit_cv.html"

    def form_valid(self, form):
        job = Job.objects.get(slug=self.request.POST.get("job_slug"))
        response = super().form_valid(form)
        cv = form.instance
        cv.candidate = self.request.user
        cv.job = job
        cv.save()
        return response


@login_required
def view_applicant_cv(request):
    if hasattr(request.user, "employer"):
        company = request.user.employer.company
        jobs = Job.objects.filter(
            company=company
        )  # Filter all the job that belongs to the company

        job_applications = {}
        for job in jobs:
            cvs = CV.objects.filter(
                job=job
            )  # Filter all the cv that applied to the job that belongs to the company
            job_applications[job] = (
                cvs  # Store the cv in the dictionary with the job as the key
            )

        return render(
            request,
            "applications/view_cv.html",
            {"job_applications": job_applications, "company": company},
        )
    return redirect("core:home")


def cv_detail(request, pk):
    cv = CV.objects.get(pk=pk)
    return render(request, "applications/cv_detail.html", {"cv": cv})


def reject_cv(request, cv_id):
    cv = CV.objects.get(pk=cv_id)
    cv.status = "Rejected"
    cv.save()

    return redirect("applications:view-applicant-cv")


def test(request):
    return render(request, "applications/searchForm.html"
                  )


def search_job(request):
    if request.method == 'GET':
        search = request.GET.get('q')
        jobs = Job.objects.filter(title__icontains=search)
        return render(request, 'applications/searchForm.html', {'jobs': jobs, 'q': search})
    else:
        return render(request, 'applications/searchForm.html')
