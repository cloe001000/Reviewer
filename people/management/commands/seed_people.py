from django.core.management.base import BaseCommand
from django_seed import Seed
from people import models


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--total", type=int, default=10, help="사람들을 뿌려드립니다 사람은 유저랑 다릅니다"
        )

    def handle(self, *args, **options):
        total = options.get("total")
        seeder = Seed.seeder()
        seeder.add_entity(models.Person, total, {"name": lambda x: seeder.faker.name()})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{total}명의 사람들을 Person모델에 만들었습니다"))