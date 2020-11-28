import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from categories import models as category_model


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            type=int,
            default=10,
            help="얼마나 많은 유저를 원하시나요? 반드시 카테고리를 먼서 Seeding해주어야 합니다",
        )

    def handle(self, *args, **options):
        Preference_Choices = (
            "books",
            "movies",
            None,
        )
        book_genres = category_model.BookCategory.objects.all()
        movie_genres = category_model.MovieCategory.objects.all()
        total = options.get("total")
        seeder = Seed.seeder()
        seeder.add_entity(
            User,
            total,
            {
                "username": lambda x: seeder.faker.name(),
                "bio": lambda x: seeder.faker.sentence(),
                "preference": lambda x: random.choice(
                    Preference_Choices
                ),  # default가 있는건 seeder가 재대로 작동을 안한다 그래서 이렇게 했다
                "Book_Genre": lambda x: random.choice(book_genres),
                "Movie_Genre": lambda x: random.choice(movie_genres),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{total}명의 유저가 생성되었습니다"))
