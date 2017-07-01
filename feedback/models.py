from django.db import models
from django.utils.translation import gettext_lazy as _

class Feedback(models.Model):
    date = models.DateField(auto_now=False,auto_now_add=True)
    user = models.ForeignKey('auth.user', blank=True)
    message = models.TextField(default='')
    
    class Meta:
        verbose_name = _("Feedback")
        verbose_name_plural = _("Feedback")
