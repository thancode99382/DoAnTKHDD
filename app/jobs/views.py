from django.shortcuts import render

from django.views import generic


# Create your views here.
class DetailJob(generic.TemplateView):
    template_name = 'jobs/detail_job.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'detalijob'
        return context
