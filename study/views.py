from rest_framework import generics, mixins, viewsets
from .permissions import IsAdminOrReadOnly
from .serializers import *


class IconsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Icons.objects.all()
    serializer_class = IconsSerializers
    permission_classes = (IsAdminOrReadOnly,)


class ImagesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializers
    permission_classes = (IsAdminOrReadOnly,)


class VideosViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Videos.objects.all()
    serializer_class = VideosSerializers
    permission_classes = (IsAdminOrReadOnly,)


class TextsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Texts.objects.all()
    serializer_class = TextsSerializers
    permission_classes = (IsAdminOrReadOnly,)


# Create your views here.
