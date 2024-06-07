from django.db import models
from django.conf import settings


# Create your models here.
class Application(models.Model):
    candidate = models.ForeignKey("users.Candidate", on_delete=models.CASCADE)
    job = models.ForeignKey("jobs.Job", on_delete=models.CASCADE)
    status = models.CharField(
        max_length=50,
        choices=[
            ("applied", "Applied"),
            ("interview", "Interview"),
            ("offer", "Offer"),
            ("rejected", "Rejected"),
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate.full_name} - {self.job.title}"

    def is_accepted(self):
        return self.status == "Accepted"


class Interview(models.Model):
    application = models.ForeignKey("Application", on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    location = models.CharField(max_length=255)
    note = models.TextField()

    def __str__(self):
        return f"{self.application.candidate.full_name} - {self.application.job.title} - {self.datetime}"


class Offer(models.Model):
    application = models.ForeignKey("Application", on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    note = models.TextField()
    status = models.CharField(max_length=255, default="Pending")

    def __str__(self):
        return f"{self.application.candidate.full_name} - {self.application.job.title} - {self.salary}"

    def is_accepted(self):
        """Check if the offer is accepted by the candidate"""
        return self.status == "Accepted"


class Feedback(models.Model):
    application = models.ForeignKey("Application", on_delete=models.CASCADE)
    note = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.application.candidate.full_name} - {self.application.job.title} - {self.created_at}"

    def is_positive(self):
        return self.rating >= 3


class CV(models.Model):
    """This CV model is used to submit for a job application."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    job = models.ForeignKey(
        "jobs.Job", on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to="cvs/")
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, default="Pending")

    def __str__(self):
        return f"{self.user.username} - {self.job.title} - {self.created_at}"
