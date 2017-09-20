from django.db import models
from django.utils.translation import gettext_lazy as _

class Updates(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=True)
    content = models.TextField(default='')
    
    class Meta:
        verbose_name = _("Updates")
        verbose_name_plural = _("Updates")
    
class Comments(models.Model):
    user = models.ForeignKey('auth.User', blank=True)
    date = models.DateField(auto_now=False, auto_now_add=True)
    message = models.TextField(default='')

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        
class Responses(models.Model):
    user = models.ForeignKey('auth.User', blank=True)
    date = models.DateField(auto_now=False, auto_now_add=True)
    message = models.TextField(default='')
    response = models.ForeignKey('Comments', blank=True)

    class Meta:
        verbose_name = _("Response")
        verbose_name_plural = _("Responses")
        
class Commenting_On(models.Model):
    active = models.BooleanField(default=False)
    class Meta:
        verbose_name = _("Comments Allowed")
        verbose_name_plural = _("Comments Allowed")
        
class Guesses(models.Model):
    user = models.ForeignKey('auth.User', blank=True)
    date = models.DateField(auto_now=False, auto_now_add=True)
    sport = models.ForeignKey('sports.Sport', blank=True, related_name = 'sport+')
    gold = models.ForeignKey('sports.Athlete', blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey('sports.Athlete', blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey('sports.Athlete', blank=True, null=True, related_name = 'bronze+')
    class Meta:
        verbose_name = _("Guess")
        verbose_name_plural = _("Guesses")