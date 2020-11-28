import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews.models import Review
from users.models import User
from books.models import Book
from movies.models import Movie


class NoneArgumentError(Exception):
    def __init__(self):
        """
        필수 명령인자가 들어오지 않았을시 발생시킬 애러 클래스 입니다
        """
        super().__init__("--kind 인자를 통해 m 또는 b 를 입력해여 책이나 영화중 종류를 골라야 합니다")
        # 부모함수에 overriding시켜야 한다


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--kind",
            default=None,
            type=str,
            help="책에 대한 리뷰:b , 영화에 대한 리뷰:m 을 입력하세요 필수 입력사항입니다",
        )
        parser.add_argument(
            "--total", default=10, type=int, help="리뷰를 얼마나 생성해보고 싶으신가요?"
        )

    def handle(self, *args, **options):
        users = User.objects.all()
        movies = Movie.objects.all()
        books = Book.objects.all()
        total = options.get("total")
        kind = options.get("kind")
        seeder = Seed.seeder()
        if kind == "b":
            b_func = lambda x: random.choice(books)
            m_func = None
        elif kind == "m":
            b_func = None
            m_func = lambda x: random.choice(movies)
        else:
            raise NoneArgumentError
        seeder.add_entity(
            Review,
            total,
            {
                "created_by": lambda x: random.choice(users),
                "text": lambda x: seeder.faker.text(),
                "rating": lambda x: random.randint(1, 10),
                "movie": m_func,
                "book": b_func,
            },
        )

        seeder.execute()
        self.stdout.write(
            self.style.SUCCESS(
                f"{total}개의 리뷰를 생성하였습니다 종류:{'책' if kind == 'b' else '영화'}"
            )
        )
