from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.views import generic
from users.forms import RecruitmentForm
from jobs.models import Company, Job


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

