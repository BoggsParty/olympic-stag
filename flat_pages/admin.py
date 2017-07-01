from django.contrib import admin
from .models import Flat_Page
from django_summernote.admin import SummernoteModelAdmin

class flat_page_admin(SummernoteModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {"slug": ("title","title",)}
    
    
admin.site.register(Flat_Page,flat_page_admin)
    
