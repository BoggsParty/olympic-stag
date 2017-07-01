from django.db import models
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _

class Flat_Page(models.Model):
    title = models.CharField(max_length=200, default='', unique=True, blank=True)
    slug = models.SlugField(default='', unique=True, blank=True)
    content = models.TextField(default='', blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("Flat Page")
        verbose_name_plural = _("Flat Pages")
