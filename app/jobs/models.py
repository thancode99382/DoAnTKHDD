from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255)
    description = CKEditor5Field('Text', config_name='extends')
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    keywords = models.ManyToManyField('Keyword')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Keyword can be represented as a tag for job
class Keyword(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # get all jobs with the keyword
    def get_jobs(self):
        return self.job_set.all()


class Company(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_job(self):
        return self.job_set.all()