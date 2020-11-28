from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.BookCategory, models.MovieCategory)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("genre",)
    list_filter = ("genre",)
