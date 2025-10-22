from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    template = "core/home_athlete.html"
    if getattr(request.user, "role", "") == "TRAINER":
        template = "core/home_trainer.html"
    return render(request, template)
