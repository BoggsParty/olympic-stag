from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, HttpResponseRedirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from sports.models import Sport
from django.template import RequestContext
from django.contrib.auth.models import User
from registration.models import Extended_User
from user_participation.models import Updates
from registration.forms import Edit_SettingsForm
from django.views.generic.edit import FormView
import datetime

@login_required
def main(request):
    sports_nav = get_list_or_404(Sport)
    score = get_list_or_404(Extended_User)
    updates = Updates.objects.all().order_by('-id')[0:5]
    now = datetime.datetime.now()
    if now.year < 2018:
        return render(request, 'main/main-with-countdown.html',{'sports_nav':sports_nav,'score':score,'updates':updates,})
    elif now.year <= 2018 and now.month <=2 and now.day <=10:
        return render(request, 'main/main-with-countdown.html',{'sports_nav':sports_nav,'score':score,'updates':updates,})
    else:
        return render(request, 'main/main.html',{'sports_nav':sports_nav,'score':score,'updates':updates,})

@login_required
def edit_settings(request):
    sports_nav = get_list_or_404(Sport)
    settings = get_object_or_404(Extended_User, user=request.user)
    if request.method == "POST":
        form = Edit_SettingsForm(request.POST,request.FILES, instance=settings)
        if form.is_valid():
            settings = form.save(commit=False)
            settings.save()
            return redirect('edit-settings')
    else:
        form = Edit_SettingsForm(instance=settings)
    return render(request, 'registration/settings.html', {'sports_nav':sports_nav,'form':form,'settings':settings})

def log_out (request):
    logout(request)
    return redirect('main')