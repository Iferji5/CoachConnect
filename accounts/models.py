from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    TRAINER = "TRAINER"
    ATHLETE = "ATHLETE"
    ROLE_CHOICES = [(TRAINER, "Entrenador"), (ATHLETE, "Alumno")]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=ATHLETE)
    timezone = models.CharField(max_length=64, default="America/Costa_Rica")
    language = models.CharField(max_length=8, default="es")

class TrainerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="trainer_profile")
    bio = models.TextField(blank=True)

class AthleteProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="athlete_profile")
    goals = models.TextField(blank=True)
