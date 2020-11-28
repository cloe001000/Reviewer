from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from core.models import TimeStampedModel

# Create your models here.


class Review(TimeStampedModel):
    """ rating은 필수로 받도록 프런트앤드 제작을 해야 함 """

    created_by = models.ForeignKey("users.User", on_delete=models.CASCADE)
    text = models.TextField(null=True)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ],
        null=True,
        # 실제로 null은 받으면 안된다, 프런트엔드에서 required로 만들자
        blank=True,
    )
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, null=True, blank=True
    )
    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"{self.created_by} : {self.text}"
