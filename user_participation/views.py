from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
#from django.views.generic import UpdateView, ListView
#from django.http import HttpResponse
#from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, get_list_or_404
from .forms import GuessForm, NewCommentForm, NewResponseForm
from sports.models import Sport, Winner
from registration.models import Extended_User
from user_participation.models import Guesses, Comments, Responses
import datetime

@login_required
#pop out window that closes on save
def guess(request, sport):
    today = datetime.datetime.now()
    now = today.date()
    lock_sports = Sport.objects.exclude(locked=True).filter(lock_date__lte=now)
    lock_sports.update(locked=True)
    sports_nav = get_list_or_404(Sport)
    sport_query = Sport.objects.get(slug=sport)
    try:
        instance = Guesses.objects.filter(sport=sport_query).get(user=request.user)
    except:
        instance = None

    if instance:
        if request.method == "POST":
            form = GuessForm(request.POST, sport=sport, instance=instance)
            if form.is_valid():
                guess = form.save(commit=False)
                guess.user = request.user
                guess.sport = sport_query
                guess.save()
                form.save_m2m()
                return redirect ('/user/guess-confirmation/')

        else:
            form = GuessForm(sport=sport, instance=instance)
            
    else:
        if request.method == "POST":
            form = GuessForm(request.POST, sport=sport)
            if form.is_valid():
                guess = form.save(commit=False)
                guess.user = request.user
                guess.sport = sport_query
                guess.save()
                form.save_m2m()
                return redirect ('/user/guess-confirmation/')

        else:
            form = GuessForm(sport=sport)
    
    return render(request, 'user_participation/guess.html',{'sports_nav':sports_nav,'form':form,'sport_query':sport_query,})

@login_required
def guess_confirmation (request):
    sports_nav = get_list_or_404(Sport)
    return render(request, 'user_participation/guess_thank_you.html',{'sports_nav':sports_nav,})

   
@login_required
#full page that redirects back to sport detail
def guess_page(request, sport):
    today = datetime.datetime.now()
    now = today.date()
    lock_sports = Sport.objects.exclude(locked=True).filter(lock_date__lte=now)
    lock_sports.update(locked=True)
    sports_nav = get_list_or_404(Sport)
    sport_query = Sport.objects.get(slug=sport)
    try:
        instance = Guesses.objects.filter(sport=sport_query).get(user=request.user)
    except:
        instance = None

    if instance:
        if request.method == "POST":
            form = GuessForm(request.POST, sport=sport, instance=instance)
            if form.is_valid():
                guess = form.save(commit=False)
                guess.user = request.user
                guess.sport = sport_query
                guess.save()
                form.save_m2m()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        else:
            form = GuessForm(sport=sport, instance=instance)
            
    else:
        if request.method == "POST":
            form = GuessForm(request.POST, sport=sport)
            if form.is_valid():
                guess = form.save(commit=False)
                guess.user = request.user
                guess.sport = sport_query
                guess.save()
                form.save_m2m()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        else:
            form = GuessForm(sport=sport)
    
    return render(request, 'user_participation/guess_new_page.html',{'sports_nav':sports_nav,'form':form,'sport_query':sport_query,})

@login_required    
def all_guess_one_user(request):
    today = datetime.datetime.now()
    now = today.date()
    lock_sports = Sport.objects.exclude(locked=True).filter(lock_date__lte=now)
    lock_sports.update(locked=True)
    sports_nav = get_list_or_404(Sport)
    guesses = Guesses.objects.filter(user=request.user)
    sport = Sport.objects.all()
    return render (request, 'user_participation/guess-all.html', {'sports_nav':sports_nav,'guesses':guesses, 'sport':sport})

@login_required    
def all_guess_all_users(request, sport):
    today = datetime.datetime.now()
    now = today.date()
    lock_sports = Sport.objects.exclude(locked=True).filter(lock_date__lte=now)
    lock_sports.update(locked=True)
    sports_nav = get_list_or_404(Sport)
    sport = get_object_or_404(Sport, slug=sport)
    guesses = Guesses.objects.filter(sport=sport)
    #sport = Sport.objects.all()
    winner = Winner.objects.get(sport=sport)
    return render (request, 'user_participation/guess-all-per-sport.html', {'sports_nav':sports_nav,'guesses':guesses, 'sport':sport, 'winner':winner,})

@login_required
def messages_first_page(request):
    sports_nav = get_list_or_404(Sport)
    extended_user = Extended_User.objects.get(user=request.user)
    messages = Comments.objects.all().order_by('-id')[:10]
    responses = Responses.objects.all()
    next_page = 1
    return render (request, 'user_participation/messages.html',{'sports_nav':sports_nav,'messages':messages,'responses':responses,'next_page':next_page, 'extended_user':extended_user,})

@login_required
def messages(request, num):
    sports_nav = get_list_or_404(Sport)
    extended_user = Extended_User.objects.get(user=request.user)
    num = int(num)
    number_10 = num+10
    next_page = num+1
    previous_page = num-1
    q_count = Comments.objects.all().count()
    final_page = q_count/10#total page count
    if q_count < 20:
        q_start = 10
        messages = Comments.objects.all().order_by('-id')[q_start:]
    else:
        q_start = q_count-(num*10)
        q_end = q_start+10
        messages = Comments.objects.all().order_by('-id')[q_start:q_end]
    responses = Responses.objects.all()
    return render (request, 'user_participation/messages.html', {'sports_nav':sports_nav,'messages':messages,'responses':responses,'next_page':next_page,'previous_page':previous_page,'final_page':final_page,'extended_user':extended_user,})

@login_required   
def new_comment(request):
    sports_nav = get_list_or_404(Sport)
    extended_user = Extended_User.objects.get(user=request.user)
    if request.method == "POST":
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('messages-first-page')
    else:
        form = NewCommentForm()
    return render(request, 'user_participation/messages-form.html', {'sports_nav':sports_nav,'form':form, 'extended_user':extended_user,})

'''
class CommentsListView(ListView):
        model = Comments
        template_name = 'user_participation/messages-form.html
        
        def get_queryset(self):
            return Comments.objects.all()
            
'''

@login_required  
def new_response(request, pk):
    sports_nav = get_list_or_404(Sport)
    extended_user = Extended_User.objects.get(user=request.user)
    response = Comments.objects.get(pk=pk)
    if request.method == "POST":
        form = NewResponseForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.response = response
            comment.save()
            return redirect('messages-first-page')
    else:
        form = NewCommentForm()
    return render(request, 'user_participation/response-messages-form.html', {'sports_nav':sports_nav,'form':form, 'extended_user':extended_user,})
'''
class CommentsUpdateView(UpdateView):
    model = Comments
    form_class = NewCommentForm
    template_name = 'user_participation/messages-form.html'
    
    def dispatch(self, *args, **kwargs):
        self.item_id = kwargs['pk']
        return super(CommentsUpdateView, self).dispatch(*args, **kwargs)
        
    def form_valid(self, form):
        form.save()
        comments = Comments.objects.get(id=self.item_id)
        return HttpResponse(render_to_string('user_participation/success.html', {'comments':comments,}))
'''

@login_required    
def edit_comment(request, pk):
    sports_nav = get_list_or_404(Sport)
    extended_user = Extended_User.objects.get(user=request.user)
    comment = get_object_or_404(Comments, pk=pk, user=request.user)
    if request.method == "POST":
        form = NewCommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('messages-first-page')
    else:
        form = NewCommentForm(instance=comment)
    return render(request, 'user_participation/messages-form.html', {'sports_nav':sports_nav,'form':form, 'extended_user':extended_user,})

@login_required    
def edit_response(request, pk):
    sports_nav = get_list_or_404(Sport)
    extended_user = Extended_User.objects.get(user=request.user)
    response = get_object_or_404(Responses, pk=pk, user=request.user)
    if request.method == "POST":
        form = NewResponseForm(request.POST, instance=response)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('messages-first-page')
    else:
        form = NewCommentForm(instance=response)
    return render(request, 'user_participation/messages-form.html', {'sports_nav':sports_nav,'form':form, 'extended_user':extended_user,})
    
'''
class AjaxTemplateMixin(object):
    def dispatch(self,request, *args, **kwargs):
        if not hasattr(self, 'ajax_template_name'):
            split = self.template_name.split('.html')
            split[-1] = '_inner'
            split.append('.html')
            self.ajax_template_name = ''.join(split)
        if request.is_ajax():
            self.template_name = self.ajax_template_name
        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)
'''