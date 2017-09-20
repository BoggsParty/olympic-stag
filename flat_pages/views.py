from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import Flat_Page
from sports.models import Sport


@login_required
def about(request):
    pages = get_list_or_404(Flat_Page)
    about = get_object_or_404(Flat_Page, slug='about')
    sports_nav = get_list_or_404(Sport)
    return render(request, 'flat_pages/about.html', {'sports_nav':sports_nav,'pages':pages,'about':about,})

@login_required
def calendar(request):
    return render(request, 'flat_pages/calendar.html',)
    
@login_required
def flat_page(request, slug):
    content = get_object_or_404(Flat_Page, slug=slug)
    sports_nav = get_list_or_404(Sport)
    return render(request, 'flat_pages/flat_page.html',{'sports_nav':sports_nav,'content':content,} )


