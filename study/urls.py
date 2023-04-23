from django.urls import path, include
from rest_framework import routers
from .views import *

app_name = 'study'

router = routers.DefaultRouter()
router.register(r'icons', IconsViewSet, basename='icons')
router.register(r'images', ImagesViewSet, basename='images')
router.register(r'videos', VideosViewSet, basename='videos')
router.register(r'texts', TextsViewSet, basename='texts')


urlpatterns = [
    path('', include(router.urls)),
]

