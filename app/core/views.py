from django.shortcuts import render

from django.views import generic

from jobs.models import Job, TopCompany, JobCategory


# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['top_jobs'] = Job.objects.all().order_by('-created_at')[:9]
        context['top_companies'] = TopCompany.objects.all()[:5]
        context['top_categories'] = JobCategory.objects.all()[:10]
        return context
