from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from jobs.models import Company
from users.forms import CustomUserCreationForm, EmployerForm, CompanyForm


# Create your views here.
class Login(LoginView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context

    def get_success_url(self):
        return reverse_lazy('core:home')


class Register(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.instance
        login(self.request, user)
        return response


class RegisterEmployer(generic.CreateView):
    form_class = EmployerForm
    success_url = reverse_lazy('core:home')
    template_name = 'users/register_employer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register Employer'
        context['company_form'] = CompanyForm()
        context['companies'] = Company.objects.all()
        return context

    def form_valid(self, form):
        employer = form.save(commit=False)
        employer.user = self.request.user
        employer.company = Company.objects.get(id=self.request.POST.get('company'))
        gender = self.request.POST.get('gender')
        gender_bool = True if gender == 'male' else False
        employer.gender = gender_bool
        # if avatar:
        #     employer.avatar = avatar
        employer.save()
        return redirect('core:home')


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('core:home')

