from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.aggregates import Count
from django_random_queryset import RandomManager

# User = get_user_model()

class ChatMessage(models.Model):
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    objects = RandomManager()
