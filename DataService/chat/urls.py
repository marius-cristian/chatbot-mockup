from django.conf.urls import include, url
from rest_framework import routers

from .views import ChatMessageViewset

api_router = routers.SimpleRouter()
api_router.register(r'chatmessages', PostViewset, base_name='chatmessage')

urlpatterns = [
    url(r'', include(api_router.urls))
]