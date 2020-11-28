from django.db import models
from core.models import TimeStampedModel

# Create your models here.


class BookCategory(TimeStampedModel):
    DETECTIVE = "detective"
    THTILLER = "thriller"
    HORROR = "horror"
    SF = "sf"
    FANTASY = "fantasy"
    MARTIAL_ARTS = "martial_arts"
    ROMENCE = "romance"
    OTHER = "other"
    Genre_Choices = (
        (DETECTIVE, "Detective"),
        (THTILLER, "Thriller"),
        (HORROR, "Horror"),
        (SF, "SF"),
        (FANTASY, "Fantasy"),
        (MARTIAL_ARTS, "Martial_arts"),
        (ROMENCE, "Romance"),
        (OTHER, "Other"),
    )
    genre = models.CharField(max_length=30, choices=Genre_Choices, default="other")

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name_plural = "Book Category"  # 클레스명+s로 자동지정되는것을 원하는 이름으로 바꾼다, 이렇게 models Meta class에 만들어준다!


class MovieCategory(TimeStampedModel):
    DETECTIVE = "detective"
    THTILLER = "thriller"
    HORROR = "horror"
    SF = "sf"
    FANTASY = "fantasy"
    MARTIAL_ARTS = "martial_arts"
    ROMENCE = "romance"
    OTHER = "other"
    Genre_Choices = (
        (DETECTIVE, "Detective"),
        (THTILLER, "Thriller"),
        (HORROR, "Horror"),
        (SF, "SF"),
        (FANTASY, "Fantasy"),
        (MARTIAL_ARTS, "Martial_arts"),
        (ROMENCE, "Romance"),
        (OTHER, "Other"),
    )

    genre = models.CharField(max_length=30, choices=Genre_Choices, default="other")

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name_plural = "Movie Category"  # 클레스명+s로 자동지정되는것을 원하는 이름으로 바꾼다, 이렇게 models Meta class에 만들어준다!
