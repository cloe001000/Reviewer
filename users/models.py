# AbstarctUser에 들어가보면 여러가지 기능들이 보인다
from categories import models as category_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # null=True 는 데이터베이스에서 공백을 혀용해준다, blank=True 는 form에서 공백을 허용해준다  , default는 기본값을 설정한다

    Preference_Choices = (
        ("books", "Books"),  # (데이터베이스에 들어갈 값, 사용자가 선택하는 값)
        ("movies", "Movies"),
        (None, "Not selected"),  # model에 None을 전달하는게 가능해보인다 -아직은-
    )

    Language_Choices = (
        ("kr", "kr"),
        ("en", "en"),
    )
    # _______________________________________________
    bio = models.TextField(default="", blank=True)
    preference = models.CharField(
        choices=Preference_Choices,
        max_length=7,
        null=True,
        blank=True,
        default="Not selected",
    )  # Char필드에 choices를 집어넣는다, choices는 선택지일 뿐,데이터베이스에는 아무런 영향이 없다=마이그레이션 불필요
    language = models.CharField(
        choices=Language_Choices, max_length=2, null=True, blank=True
    )
    Book_Genre = models.ForeignKey(
        category_model.BookCategory, on_delete=models.CASCADE, null=True
    )
    Movie_Genre = models.ForeignKey(
        category_model.MovieCategory, on_delete=models.CASCADE, null=True
    )
