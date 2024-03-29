from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from .models import ScoreBoard
from .forms import EditScoresForm

from ..events.forms import CreateEventForm

def edit_scores_view(request, event_id):
    scoreboard = get_object_or_404(ScoreBoard, event_id=event_id)
    if request.method == "POST" and request.POST.get("event_info"):
        event_form = CreateEventForm(request.POST, instance=scoreboard.event)
        if event_form.is_valid():
            event_form.save()
            messages.info(request, "Event edited!")
            return redirect(reverse("index"))
    else:
        event_form = CreateEventForm(instance=scoreboard.event)
    if request.method == "POST" and request.POST.get("event_score"):
        form = EditScoresForm(request.POST, instance=scoreboard)
        if form.is_valid():
            form.save()
            messages.info(request, "Event scores edited!")
            return redirect(reverse("index"))
    else:
        form = EditScoresForm(instance=scoreboard)
    context = {"event_form": event_form, "score_form": form, "scoreboard": scoreboard}
    return render(request, "edit_scores_page.html", context)
