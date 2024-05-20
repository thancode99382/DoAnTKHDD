from django.db import models


# Create your models here.
class Candidate(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar_candidate/', null=True, blank=True)
    phone = models.CharField(max_length=20)
    cv = models.FileField(upload_to='cv/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_name(self):
        return self.user.get_full_name()

    def __str__(self):
        return self.get_name()


class Employer(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar_employer/', null=True, blank=True)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey('jobs.Company', on_delete=models.CASCADE)

    def get_name(self):
        return self.user.get_full_name()

    def __str__(self):
        return self.get_name()
