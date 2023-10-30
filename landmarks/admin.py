from django.contrib import admin

from .models import Landmark, Comment, Image

class ImageInline(admin.StackedInline):
    model = Image
    extra = 0

@admin.register(Landmark)
class LandmarkAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Comment)