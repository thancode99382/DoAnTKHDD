from django.shortcuts import render

from django.views import generic


# Create your views here.
class Company(generic.TemplateView):
    template_name = 'applications/company.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'detalijob'
        return context
