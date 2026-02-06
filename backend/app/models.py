from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    last_login_custom = models.DateTimeField(null=True, blank=True)
    date_registered = models.DateTimeField(auto_now_add=True)
    is_active_now = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} Profile"

class Note(models.Model): 
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title