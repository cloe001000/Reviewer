from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "kind",
    )
    list_filter = ("kind",)
    search_fields = ("name",)