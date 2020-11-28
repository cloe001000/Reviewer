import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from movies import models as movie_model
from categories import models as category_model
from people import models as person_model


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--total", type=int, default=10, help="영화를 몇편 생성하고 싶나요?")

    def handle(self, *args, **options):
        genre = category_model.MovieCategory.objects.all()
        people = person_model.Person.objects.all()
        total = options.get("total")
        seeder = Seed.seeder()
        seeder.add_entity(
            movie_model.Movie,
            total,
            {
                "genre": lambda x: random.choice(genre),
                "year": lambda x: random.randint(1900, 2030),
                "director": lambda x: random.choice(people),
            },
        )
        pks = seeder.execute()
        print(
            f"생성되는 오브젝트들의 ID입니다 {list(pks.values())[0]} ManyToMany필드가 포함되어 있으므로 출력합니다. \n 해당필드 : Actor"
        )
        cleand_pks = flatten(list(pks.values()))
        for pk in cleand_pks:
            select_movie = movie_model.Movie.objects.get(pk=pk)
            to_add_actors = people[0 : random.randint(2, 10)]
            select_movie.actor.add(*to_add_actors)
        self.stdout.write(self.style.SUCCESS(f"{total}편의 영화가 만들어졌습니다"))
