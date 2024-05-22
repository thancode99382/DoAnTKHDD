from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Select
from django.utils.text import slugify

from jobs.models import Company, Job, Keyword
from .models import *


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('phone', 'avatar', 'company', 'position', 'work_location', 'full_name')
        exclude = ('user',)
        widgets = {
            'position': Select(attrs={'class': 'pl-3 pr-4 py-2 border rounded-lg w-full'}),
            'work_location': Select(attrs={'class': 'pl-3 pr-4 py-2 border rounded-lg w-full'}),
        }


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'logo', 'description', 'address', 'phone', 'email')
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'block w-full mt-2 p-2 border rounded-md focus:border-blue-500 focus:ring-blue-500'}),
            'logo': forms.FileInput(
                attrs={'class': 'block w-full mt-2 p-2 border rounded-md focus:border-blue-500 focus:ring-blue-500'}),
            'description': forms.Textarea(
                attrs={'class': 'block w-full mt-2 p-2 border rounded-md focus:border-blue-500 focus:ring-blue-500',
                       'rows': 5}),
            'address': forms.TextInput(
                attrs={'class': 'block w-full mt-2 p-2 border rounded-md focus:border-blue-500 focus:ring-blue-500'}),
            'phone': forms.TextInput(
                attrs={'class': 'block w-full mt-2 p-2 border rounded-md focus:border-blue-500 focus:ring-blue-500'}),
            'email': forms.EmailInput(
                attrs={'class': 'block w-full mt-2 p-2 border rounded-md focus:border-blue-500 focus:ring-blue-500'}),
        }
        labels = {
            'name': 'Tên công ty',
            'logo': 'Logo',
            'description': 'Mô tả',
            'address': 'Địa chỉ',
            'phone': 'Số điện thoại',
            'email': 'Email',
        }


class RecruitmentForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'company', 'keywords', 'category', 'salary_min', 'salary_max']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        employer = Employer.objects.get(user=user)
        super(RecruitmentForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
        self.fields['company'].queryset = Company.objects.filter(id=employer.company.id)
        self.fields['keywords'].queryset = Keyword.objects.filter(name=employer.get_work_location_display())

    def save(self):
        slug = slugify(self.cleaned_data['title'])
        self.instance.slug = slug
        return super(RecruitmentForm, self).save()