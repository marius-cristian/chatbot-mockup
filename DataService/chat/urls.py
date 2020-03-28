from django.conf.urls import include, url
from rest_framework import routers

from .views import ChatMessageViewset
from .views import RandomChatMessage

api_router = routers.SimpleRouter()
api_router.register(r'chatmessages', ChatMessageViewset, basename='chatmessage')
api_router.register(r'random', RandomChatMessage, basename='randommessage')

urlpatterns = [
    url(r'', include(api_router.urls))
]