from django.shortcuts import redirect
from applications.models import CV
from applications.forms import CVForm

from users.forms import CompanyForm
from .models import *

from django.views import generic


# Create your views here.
class DetailJobView(generic.DetailView):
    model = Job
    template_name = "jobs/detail_job.html"
    context_object_name = "job"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Detail Job"
        context["CVForm"] = CVForm()
        return context


class TopJobView(generic.TemplateView):
    template_name = "jobs/top_jobs.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Job"
        context["top_jobs"] = Job.objects.all().order_by("-created_at")[:5]
        # context['top_categories'] = JobCategory.objects.all()[:5]
        return context


def create_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("users:register-employer")
    return redirect("core:home")
