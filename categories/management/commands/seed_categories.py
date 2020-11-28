import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from categories import models as category_model


class Command(BaseCommand):

    help = "카테고리 뿌리기!"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total", default=10, type=int, help="얼마나 많은 수를 원하는지 입력해주세요"
        )
        parser.add_argument(
            "--kind",
            default="",
            type=str,
            help="종류를 선택하여 뿌릴 수 있습니다. 책은 'b', 영화는 'm' 을 입력해주세요",
        )

    def handle(self, *args, **options):
        DETECTIVE = "detective"
        THTILLER = "thriller"
        HORROR = "horror"
        SF = "sf"
        FANTASY = "fantasy"
        MARTIAL_ARTS = "martial_arts"
        ROMENCE = "romance"
        OTHER = "other"
        Genre_Choices = (  # defoult가 설정되어있다면 seeder가 렌덤하게 못뿌리는것으로 보인다
            DETECTIVE,
            THTILLER,
            HORROR,
            SF,
            FANTASY,
            MARTIAL_ARTS,
            ROMENCE,
            OTHER,
        )
        total = options.get("total")
        kind = options.get("kind")
        seeder = Seed.seeder()
        if kind == "b":
            seeder.add_entity(
                category_model.BookCategory,
                total,
                {
                    "genre": lambda x: random.choice(Genre_Choices),
                },
            )
        elif kind == "m":
            seeder.add_entity(
                category_model.MovieCategory,
                total,
                {
                    "genre": lambda x: random.choice(Genre_Choices),
                },
            )
        else:
            seeder.add_entity(
                category_model.MovieCategory,
                total,
                {
                    "genre": lambda x: random.choice(Genre_Choices),
                },
            )
            seeder.add_entity(
                category_model.BookCategory,
                total,
                {
                    "genre": lambda x: random.choice(Genre_Choices),
                },
            )
        seeder.execute()
        self.stdout.write(
            self.style.SUCCESS(
                f"총 {total}개의 카테고리가 생성되었습니다 속성:{'책 추가!' if kind == 'b' else ('영화 추가!' if kind == 'm' else '책,영화 모두 해당 수 만큼 추가되었습니다')}"
            )
        )
