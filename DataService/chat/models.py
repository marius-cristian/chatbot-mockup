from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.aggregates import Count

# User = get_user_model()

class ChatMessage(models.Model):
    # id = models.AutoField(primary_key=True) #models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

from django.db.models.aggregates import Count