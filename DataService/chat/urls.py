from django.conf.urls import include, url
from rest_framework import routers

from .views import StandardViewSet
from .views import RandomViewSet

api_router = routers.SimpleRouter()
api_router.register(r'chatmessages', StandardViewSet, basename='chatmessage')
api_router.register(r'random', RandomViewSet, basename='randommessage')

urlpatterns = [
    url(r'', include(api_router.urls))
]