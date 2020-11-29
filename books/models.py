from functools import reduce

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from core.models import TimeStampedModel

# Create your models here.


class Book(TimeStampedModel):
    title = models.CharField(max_length=50)
    plot = models.TextField(null=True)
    year = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2030),
        ],  # 이것은 IntegerField에서 Input을 제한해서 받을수 있는 방법이다
    )
    cover_image = models.ImageField(null=True, blank=True)
    genre = models.ForeignKey(
        "categories.BookCategory",
        on_delete=models.CASCADE,
        default="other",
        # Foreignkey 에는 null이나 blank나 default가 필요하다
    )
    writer = models.ForeignKey(
        "people.Person",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def total_rating(self):
        # 모델 역참조를 통해 이 책의 평균rating을 구해낸다 Review모델을 import하여 필터링 하는것이 아니다
        all_reviews = self.review_set.all()
        # 이 모델이 가지고 있는 _set을 이용해 해당되는 리뷰를 포인팅해둔다
        sum = reduce(lambda acc, review: acc + review.rating, all_reviews, 0)
        # 쿼리를 피누산자로 사용해 review.rating을 0에 계속 더해준다
        if not len(all_reviews):
            return "No reviews"
            # if 0=False->(not:반전) 을 통해 리뷰가 없으면 No reviews를 대신 리턴한다
            # false일 경우 라고 생각해
        return round(sum / len(all_reviews), 2)
        # 리뷰가 있을시 평균을 구하여 리턴한다
