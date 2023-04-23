from django.contrib import admin
from .models import Icons, Images, Videos, Texts


class IconsAdmin(admin.ModelAdmin):
    list_display = ('id', 'icons')


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'images')


class VideosAdmin(admin.ModelAdmin):
    list_display = ('id', 'urls')
    list_display_links = ('id', 'urls')


class TextsAdmin(admin.ModelAdmin):
    list_display = ('id', 'texts')


admin.site.register(Icons, IconsAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Texts, TextsAdmin)
admin.site.register(Videos, VideosAdmin)

# Register your models here.
