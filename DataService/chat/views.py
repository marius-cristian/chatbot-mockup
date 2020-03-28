from django.shortcuts import render

from rest_framework import viewsets

from .models import ChatMessage
from .serializer import ChatMessageSerializer


class BaseViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return self.model.objects.all()

# must refactor to pass parameter for example: 
class ChatMessageViewset(BaseViewSet):
    serializer_class = ChatMessageSerializer
    model = ChatMessage




# must refactor this, its duplicate code
class RandomViewSet(viewsets.ModelViewSet):
    def get_queryset(self):

        return self.model.objects.filter().random()


class RandomChatMessage(RandomViewSet):
    serializer_class = ChatMessageSerializer
    model = ChatMessage