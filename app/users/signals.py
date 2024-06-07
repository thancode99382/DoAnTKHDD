# myapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Candidate, Employer

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_employer:
            Employer.objects.create(user=instance)
        else:
            Candidate.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'employer'):
        instance.employer.save()
    elif hasattr(instance, 'candidate'):
        instance.candidate.save()
