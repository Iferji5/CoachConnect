from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

class Excercise(models.Model):
    name = models.CharField(max_length=120)
    muscle_group = models.CharField(max_length=120, blank=False, null=False)
    level = models.CharField(max_length=120, blank=True, null=False)
    equipment = models.CharField(max_length=120, blank=True, null=False)

    def __str__(self):
        return self.excercise

class ExerciseVideo(models.Model):
   exercise = models.ForeignKey(Excercise, on_delete=models.CASCADE, related_name="video")
   url = models.URLField()
   provider = models.CharField(max_length=120, blank=False, null=False)
   duration = models.IntegerField()

   def __str__(self):
       return f'Video {self.provider or ''} de {self.excercise.name}'


class Plan (models.Model):
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="plans")
    title = models.CharField(max_length=120)
    goal = models.TextField(max_length=120, blank=True)
    weeks = models.PositiveSmallIntegerField(default=4)
    def __str__(self):
        return self.title


class PlanExercise(models.Model):
    DAYS = [(i, d) for i,d in enumerate(["Lun","Mar","Mie","Jue","Vie","Sab","Dom"], start=1)]
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="items")
    exercise = models.ForeignKey(Excercise, on_delete=models.CASCADE)
    day_of_week = models.PositiveSmallIntegerField(choices=DAYS)
    sets = models.PositiveSmallIntegerField(default=3)
    reps = models.PositiveSmallIntegerField(default=10)
    rest_seconds = models.PositiveSmallIntegerField(default=60)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["day_of_week", "id"]

    def __str__(self):
        return f"{self.plan.title} {self.exercise.name} ({self.get_day_of_week_display()})"


# Create your models here.

