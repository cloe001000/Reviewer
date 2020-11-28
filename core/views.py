from django.shortcuts import render
from movies import models as movie_model
from books import models as book_model
from reviews import models as review_model

# Create your views here.


def main_page(request):

    movies = movie_model.Movie.objects.all().order_by("-year")[:10]
    # total_rating을 order_by에 사용할수 없다 우선 최신연도순 정렬 10개 추출
    books = book_model.Book.objects.all().order_by("-year")[:10]
    movies_data = []
    books_data = []
    for movie, book in zip(movies, books):
        # 최신 10개 항목들을 total_rating으로 정렬
        movies_data.append((movie.total_rating(), movie))
        books_data.append((book.total_rating(), book))
    sorted_movies_list = sorted(movies_data, key=lambda x: x[0])
    # ,(평점,객체),,, 로 저장된 자료형이지만 sort 함수가 먹혀 든다
    sorted_books_list = sorted(books_data, key=lambda x: x[0])

    # ------최신 연도순으로 10개 선별 후 평균평점순으로 정렬 완료-----------

    movie_review_list = []
    # sorted_movies_list와 대응되는 리뷰리스트이며 각 요소는 [(상위3쿼리셋),(하위3쿼리셋)] 으로 구성되어있다
    book_review_list = []
    for movie in sorted_movies_list:
        top_3 = movie[1].review_set.field.model.objects.all().order_by("-rating")[:3]
        bottom_3 = movie[1].review_set.field.model.objects.all().order_by("rating")[:3]
        movie_review_list.append([top_3, bottom_3])
        # top_3,bottom_3 는 둘다 쿼리셋이다
    for book in sorted_books_list:
        top_3 = book[1].review_set.field.model.objects.all().order_by("-rating")[:3]
        bottom_3 = book[1].review_set.field.model.objects.all().order_by("rating")[:3]
        book_review_list.append([top_3, bottom_3])
        # top_3,bottom_3 는 둘다 쿼리셋이다

    # -------각각 영화,책과 대응하는 상위리뷰3개,하위리뷰3개 단위의 리뷰리스트 생성 완료-----

    return render(
        request,
        "main.html",
        {
            "movie_data": zip(sorted_movies_list, movie_review_list),
            "book_data": zip(sorted_books_list, book_review_list),
        },
        # for문 안에서 -> movie_data[0] = 영화, movie_data[1] = 그 영화에 대한 리뷰DATA, movie_data[1][0] = 상위3개리뷰 쿼리셋 , movie_data[1][1] = 하위3개리뷰 쿼리셋
    )
