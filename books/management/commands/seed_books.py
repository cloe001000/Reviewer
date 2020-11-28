import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from books.models import Book
from categories.models import BookCategory
from people.models import Person


class Command(BaseCommand):
    help = "책 뿌리기! ㅎㅎ"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            help="책 몇권을 만들어 뿌릴지 결정해주세요!",
            default=10,
            type=int,
        )

    def handle(self, *args, **options):
        total = options.get("total")
        genre = BookCategory.objects.all()
        writer = Person.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(
            Book,
            total,
            {
                "genre": lambda x: random.choice(genre),
                "writer": lambda x: random.choice(writer),
                # 실수 렌덤값은 uniform을 통해 얻는다! , round를 사용해 자릿수를 제한한다!
                # rating은 자동생성되므로 seeding하지 않는다
                "year": lambda x: random.randint(1900, 2030),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{total}권의 책들이 만들어졌습니다!"))
