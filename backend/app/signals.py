from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import *
from django.utils import timezone

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def update_last_login(sender, instance, **kwargs):
    # Update last_login_custom whenever user is saved... after login
    if instance.profile:
        instance.profile.last_login_custom = timezone.now()
        instance.profile.save()