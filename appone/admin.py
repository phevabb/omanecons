from django.contrib import admin
from django.utils.html import format_html
from .models import *


@admin.register(Handyman)
class HandymanAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag',)  # show image in list view

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image.url)
        return "(No image)"

    image_tag.short_description = 'Image'




@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag',)  # show image in list view

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image.url)
        return "(No image)"

    image_tag.short_description = 'Image'



@admin.register(Logistic)
class LogisticAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag',)  # show image in list view

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image.url)
        return "(No image)"

    image_tag.short_description = 'Image'