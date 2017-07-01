from django.contrib import admin
from .models import Feedback

class Feedback_admin(admin.ModelAdmin):
    list_display = ('date','user',)
    filter_by = ('user',)
    
admin.site.register(Feedback,Feedback_admin)
