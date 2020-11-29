from django.shortcuts import render
from . import models as movie_model
from core.custom_package import (
    sorted_cut,
    sort_by_total_rating,
    sorted_by_total_rating_form_review,
)

# Create your views here.


def movie_main(request):
    page = int(request.GET.get("page", 1) or 1)
    # 말 그대로 request를 GET 메소드로 받아낸다 QueryDict으로 가공된것을 넘겨받는다
    # QueryDict.get()을 사용할수 있따 dir(QueryDict)로 본다
    page_size = 20
    page_count = int(movie_model.Movie.objects.count() / page_size) + 1
    limit = page_size * page
    offset = limit - page_size
    movies = sorted_cut(movie_model.Movie, "year", offset, limit)
    set_movies = sort_by_total_rating(movies)
    set_review = [
        sorted_by_total_rating_form_review(movie[1], 5) for movie in set_movies
    ]
    # 가로5 X 세로4 로 배치, Nav는 수직으로 세워서 배치

    return render(
        request,
        "movies/main.html",
        {
            "movie_data": zip(set_movies, set_review),
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count + 1),
        },
    )


def movie_detail(request):
    return render(request, "movies/detail.html", {})
