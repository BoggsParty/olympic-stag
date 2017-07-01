from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm
from .models import Feedback
import datetime

@login_required
def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('/')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedbackform.html', {'form':form})
    