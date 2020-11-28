from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("created_by", "book", "movie", "rating")
    search_fields = ("created_by__username", "movie__title", "book__title")
    list_filter = ("rating", "book", "movie")
