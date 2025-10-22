from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, TrainerProfile, AthleteProfile

@receiver(post_save, sender=User)
def create_profiles(sender, instance, created, **kwargs):
    if created:
        if instance.role == User.TRAINER:
            TrainerProfile.objects.create(user=instance)
        else:
            AthleteProfile.objects.create(user=instance)
