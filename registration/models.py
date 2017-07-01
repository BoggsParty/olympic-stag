from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

class Extended_User(models.Model):
    user = models.OneToOneField('auth.User')
    avatar = models.ImageField(upload_to='avatars', blank=True)
    score = models.IntegerField(default='0')
    forbidden = models.BooleanField(default=False)
    email = models.EmailField(default='')
    notifications = models.BooleanField(default=False)
    
    #def __str__(self):
        #return self.user
        
    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")

@receiver(post_save, sender=User)
def create_extended_user(sender, instance, created, **kwargs):
    if created:
        Extended_User.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def save_extended_user(sender, instance, **kwargs):
    instance.extended_user.save()