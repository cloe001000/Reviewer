import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from favlists import models as favlist_model
from books import models as book_model
from movies import models as movie_model
from users.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--total", type=int, default=10, help="Favorit리스트를 몇개 만들고 싶나요?"
        )

    def handle(self, *args, **options):
        books = book_model.Book.objects.all()
        movies = movie_model.Movie.objects.all()
        users = User.objects.all()
        total = options.get("total")
        seeder = Seed.seeder()
        seeder.add_entity(
            favlist_model.FavList,
            total,
            {
                "list_name": lambda x: seeder.faker.name(),
                "created_by": lambda x: random.choice(users),
            },
        )
        pks = seeder.execute()
        # seeder가 row에 데이터를 뿌리고 그 데이터들의 아이디 리스트를 반환해준다
        print(
            f"생성되는 오브젝트들의 ID입니다 {list(pks.values())[0]} ManyToMany필드가 포함되어 있으므로 출력합니다. \n해당필드: movie,book"
        )  # flatton 쓰나 이렇게 하나...같아
        # {<class 'favlists.models.FavList'>: [87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]}
        cleaned_pks = flatten(list(pks.values()))
        # values해줘도 [[값 리스트]]이므로 이렇게 처리해준다
        for pk in cleaned_pks:
            # seeder가 만든 쿼리들의 키들로 for문을 돌려가면서 렌덤으로 슬라이스해서 ManyToManyField에 추가해준다
            select_favlist = favlist_model.FavList.objects.get(pk=pk)
            to_add_movies = movies[0 : random.randint(2, 10)]
            to_add_books = books[0 : random.randint(2, 10)]
            select_favlist.book.add(*to_add_books)
            # add를 사용하면 모델 안의 필드를 선택적으로 채울수 있다 (book필드를 선택)
            select_favlist.movie.add(*to_add_movies)
            # add는 *args인자를 받기 때문에 이렇게 언팩해서 줄수 있다

        self.stdout.write(self.style.SUCCESS(f"{total}개의 favlist들이 생성되었습니다"))
