from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import Sport, Sport_Images, Winner
from user_participation.models import Guesses
import datetime

@login_required
def sport_menu(request):
    today = datetime.datetime.now()
    now = today.date()
    lock_sports = Sport.objects.exclude(locked=True).filter(lock_date__lte=now)
    lock_sports.update(locked=True)
    sport = get_list_or_404(Sport)
    sports_nav = get_list_or_404(Sport)
    return render(request, 'sports/sport_menu.html',{'sport':sport,'sports_nav':sports_nav,})

@login_required
def sport_detail(request, sport):
    today = datetime.datetime.now()
    now = today.date()
    lock_sports = Sport.objects.exclude(locked=True).filter(lock_date__lte=now)
    lock_sports.update(locked=True)
    sport = get_object_or_404(Sport, slug=sport)
    images = get_list_or_404(Sport_Images, sport=sport)
    sports_nav = get_list_or_404(Sport)
    
    completed = True
    try:
        winner = Winner.objects.get(sport=sport)
    except:
        winner = None
        completed = False

    try:
        guesses = Guesses.objects.filter(sport=sport).get(user=request.user)
        guess_set= True
    except:
        guesses = None
        guess_set = False
    return render(request, 'sports/sport_detail.html',{'sports_nav':sports_nav,'sport':sport, 'images':images,'completed':completed,'guesses':guesses,'winner':winner})
