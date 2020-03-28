from django.shortcuts import render

from rest_framework import viewsets

from .models import ChatMessage
from .serializers import ChatMessageSerializer


class BaseViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return self.model.objects.all()


class ChatMessageViewset(BaseViewSet):
    serializer_class = ChatMessageSerializer
    model = ChatMessage