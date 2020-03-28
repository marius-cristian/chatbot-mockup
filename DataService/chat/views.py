from django.shortcuts import render

from rest_framework import viewsets

from .models import ChatMessage
from .serializer import ChatMessageSerializer

from rest_framework.decorators import action

class BaseViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return self.model.objects.all()



# must refactor to pass parameter for example: 
class ChatMessageViewset(BaseViewSet):
    serializer_class = ChatMessageSerializer
    model = ChatMessage

    #@action(detail=True, methods=['get'])
    #def retrieve(self, request):
    #    queryset = self.model.objects.filter().random()
    #    user = get_object_or_404(queryset)
    #    serializer = ChatMessageSerializer(user)
    #    return Response(serializer.data)



# must refactor this, its duplicate code
# I don know if its optimal (do not know what is happening
# in django_random_queryset RandomManager under the hood)
class RandomViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return self.model.objects.filter().random()


class RandomChatMessage(RandomViewSet):
    serializer_class = ChatMessageSerializer
    model = ChatMessage