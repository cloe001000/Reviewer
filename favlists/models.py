from django.db import models
from core.models import TimeStampedModel

# Create your models here.
# 이니셜 마이그레이션을 생성할떄는 마이그레이트가 자동으로 된다


class FavList(TimeStampedModel):
    created_by = models.ForeignKey("users.User", on_delete=models.CASCADE)
    list_name = models.CharField(max_length=30, default="My favorite list")
    book = models.ManyToManyField("books.Book")  # ManyToMany는 on_delete가 필요 없다
    movie = models.ManyToManyField("movies.Movie")

    def __str__(self):
        return f"{self.created_by}'s favorite list -  {self.pk}"
