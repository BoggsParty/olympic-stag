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
from user_participation.models import Scores
import datetime

#@login_required
def main(request):
    #sports_nav = get_list_or_404(Sport)
    #score = scores.objects.all().order_by('-score')
    updates = Updates.objects.all().order_by('-id')[0:5]
    now = datetime.datetime.now()
    #if now.year < 2018:
       # return render(request, 'main/main-with-countdown.html',{'sports_nav':sports_nav,'score':score,'updates':updates,})
    #if now.year == 2018 and now.month <=2 and now.day <=10:
    if now.year < 2020:
        return render(request, 'main/countdown-only.html',{'updates':updates,})
    elif now.year == 2020 and now.month < 7:
        return render(request, 'main/main-with-countdown.html',{'updates':updates,})
        #return render(request, 'main/main-with-countdown.html',{'score':score,'updates':updates,})
    elif now.year == 2020 and now.month ==7 and now.day <25:    
        return render(request, 'main/main-with-countdown.html',{'score':score,'updates':updates,})
    else:
        return render(request, 'main/main.html',{'score':score,'updates':updates,})

@login_required
def edit_settings(request):
    #sports_nav = get_list_or_404(Sport)
    settings = get_object_or_404(Extended_User, user=request.user)
    if request.method == "POST":
        form = Edit_SettingsForm(request.POST,request.FILES, instance=settings)
        if form.is_valid():
            settings = form.save(commit=False)
            settings.save()
            return redirect('edit-settings-saved')
    else:
        form = Edit_SettingsForm(instance=settings)
    return render(request, 'registration/settings.html', {'form':form,'settings':settings})

def edit_settings_saved(request):
    #sports_nav = get_list_or_404(Sport)
    settings = get_object_or_404(Extended_User, user=request.user)
    if request.method == "POST":
        form = Edit_SettingsForm(request.POST,request.FILES, instance=settings)
        if form.is_valid():
            settings = form.save(commit=False)
            settings.save()
            return redirect('edit-settings-saved')
    else:
        form = Edit_SettingsForm(instance=settings)
    return render(request, 'registration/settings-saved.html', {'form':form,'settings':settings})
    
def password_reset(request):
    return render(request, 'registration/password-reset.html',)
    
def log_out (request):
    logout(request)
    return redirect('main')
    
def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response