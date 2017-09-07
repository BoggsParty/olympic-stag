from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Country, Sport, Athlete, Winner, Sport_Images
#from django_summernote.admin import SummernoteModelAdmin

class CountryResource(resources.ModelResource):
    class Meta:
        model = Country

class country_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display  = ('country', 'abbreviation',)

admin.site.register(Country,country_admin)


class SportResource(resources.ModelResource):
    class Meta:
        model = Sport

#class sport_admin(SummernoteModelAdmin):
class sport_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display  = ('sport_name', 'lock_date',)
    prepopulated_fields = {"slug": ("sport_name",)}

admin.site.register(Sport,sport_admin,)

class AthleteResource(resources.ModelResource):
    class Meta:
        model = Athlete

class athlete_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('athlete_name','country',)

admin.site.register(Athlete,athlete_admin)

class WinnerResource(resources.ModelResource):
    class Meta:
        model = Winner

class winner_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('sport',)

admin.site.register(Winner,winner_admin)
'''
class team_winner_admin(admin.ModelAdmin):
    list_display = ('sport',)

admin.site.register(Team_Winner,team_winner_admin)
'''
class sport_images_admin(admin.ModelAdmin):

    list_display = ('title','active','sport')

admin.site.register(Sport_Images,sport_images_admin)