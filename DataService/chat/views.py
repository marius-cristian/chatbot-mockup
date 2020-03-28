from django.shortcuts import render

from rest_framework import viewsets

from .models import ChatMessage
from .serializer import ChatMessageSerializer

from rest_framework.decorators import action

class BaseViewSet(viewsets.ModelViewSet):
    serializer_class = ChatMessageSerializer
    model = ChatMessage



class StandardViewSet(BaseViewSet):
    def get_queryset(self):
        return self.model.objects.all()


class RandomViewSet(BaseViewSet):
    def get_queryset(self):
        return self.model.objects.filter().random()
