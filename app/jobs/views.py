from django.views import generic

from .models import *


from django.views import generic


# Create your views here.
class DetailJob(generic.TemplateView):
    template_name = 'jobs/detail_job.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'detalijob'
        return context
class TopJobView(generic.TemplateView):
    template_name = 'jobs/top_jobs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Job'
        context['top_jobs'] = Job.objects.all().order_by('-created_at')[:5]
        # context['top_categories'] = JobCategory.objects.all()[:5]
        return context
