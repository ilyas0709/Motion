from modeltranslation.utils import build_localized_fieldname
from rest_framework import serializers
from .models import *


class IconsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Icons
        fields = 'id icons'.split()


class ImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = 'id images'.split()


class TextsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Texts
        fields = 'id texts'.split()


class VideosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = 'id urls'.split()