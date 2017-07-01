from django.contrib import admin
from .models import Comments, Responses, Commenting_On, Guesses, Updates

class Updates_admin(admin.ModelAdmin):
    list_display = ('date',)
    
admin.site.register(Updates, Updates_admin)

class Comments_admin(admin.ModelAdmin):
    list_display = ('user', 'date',)
    
admin.site.register(Comments,Comments_admin)

class Responses_admin(admin.ModelAdmin):
    list_display = ('user', 'date',)
    
admin.site.register(Responses, Responses_admin)

class Commenting_On_admin(admin.ModelAdmin):
    list_display = ('pk','active')
    
admin.site.register(Commenting_On,Commenting_On_admin)

class Guesses_admin(admin.ModelAdmin):
    list_display = ('user','sport','date',)
    order = ('date')
    filter_by = ('sport','user')

admin.site.register(Guesses, Guesses_admin)