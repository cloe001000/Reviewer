from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "total_rating",
        "genre",
        "director",
        "year",
        "created",
    )

    list_filter = (
        "genre",
        "director",
    )

    ordering = [
        "year",
    ]
    # 이것들에 대해서 정렬할수 있는 기능이 생긴다
    search_fields = ("title", "^year", "pk")
    # filter가 되는것은 넣을필요 없다
    # year는 명백히 int형이므로 거의 별계의 검색창처럼 사용할수 있게 하였다
    filter_horizontal = ("actor",)
