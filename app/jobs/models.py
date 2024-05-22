from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class HurryJob(models.Model):
    job = models.OneToOneField('Job', on_delete=models.CASCADE)
    is_hurry = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        if self.is_hurry:
            return "Gấp".upper()


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = CKEditor5Field('Text', config_name='extends')
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    # salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    keywords = models.ManyToManyField('Keyword')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    category = models.ForeignKey('JobCategory', on_delete=models.CASCADE, null=True, blank=True)
    experience_min = models.IntegerField(null=True, blank=True)
    experience_max = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    def salary_written_in_text(self):
        """Return salary in text format"""
        if self.salary_min is None and self.salary_max is None:
            return "Thỏa thuận"

        salary_min_str = str(self.salary_min)
        salary_max_str = str(self.salary_max)
        if self.salary_min and self.salary_max is None:
            return f'Trên {salary_min_str[:2]} triệu'
        if self.salary_min is None and self.salary_max:
            return f'Dưới {salary_max_str[:2]} triệu'
        return f'{salary_min_str[:2]} - {salary_max_str[:2]} triệu'

    def get_experience_year(self):
        if self.experience_min is None and self.experience_max is None:
            return "Không yêu cầu kinh nghiệm"
        if self.experience_min is None and self.experience_max:
            return f"Tối thiểu {self.experience_max} năm"
        if self.experience_min and self.experience_max is None:
            return f"Trên {self.experience_min} năm"
        return f"{self.experience_min} - {self.experience_max} năm"


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
    email = models.EmailField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    description = CKEditor5Field('Text', config_name='extends', null=True, blank=True)
    logo = models.ImageField(upload_to='companies/', null=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_job(self):
        return self.job_set.all()


class TopCompany(models.Model):
    company = models.OneToOneField('Company', on_delete=models.CASCADE)

    def __str__(self):
        return self.company.name


class JobCategory(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)

    def __str__(self):
        return self.name

    def job_counts(self):
        return self.job_set.count()
