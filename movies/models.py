from functools import reduce
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from core.models import TimeStampedModel

# Create your models here.


class Movie(TimeStampedModel):
    title = models.CharField(max_length=30)
    genre = models.ForeignKey(
        "categories.MovieCategory",
        on_delete=models.CASCADE,
    )
    year = models.IntegerField(
        null=True,
        validators=[
            MaxValueValidator(2030),
            MinValueValidator(1900),
        ],
    )
    cover_image = models.ImageField(null=True, blank=True)
    actor = models.ManyToManyField(
        "people.Person", blank=True, related_name="movie_actor"
    )
    # ManyToMnay에서 null은 하나마나다`
    director = models.ForeignKey(
        "people.Person",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="movie_director",
    )

    def __str__(self):
        return self.title

    def total_rating(self):
        all_reviews = self.review_set.all()
        sum = reduce(lambda acc, review: acc + review.rating, all_reviews, 0)
        if not len(all_reviews):
            return "No reviews"
        return round(sum / len(all_reviews), 2)