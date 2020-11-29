from django.shortcuts import render, redirect
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


def movie_detail(request, pk):
    page = int(request.GET.get("page", 0) or 0)
    # 일단은 리뷰 더보기 기능으로 생각
    model = movie_model.Movie.objects.get(pk=pk)
    total_rating = model.total_rating()
    reviews = model.review_set.all()
    page_size = 20
    main_page_size = 5
    page_count = int((movie_model.Movie.objects.count() - main_page_size) / page_size)
    limit = (page * page_size) + main_page_size
    offset = limit - page_size if limit > main_page_size else 0
    review_data = reviews.order_by("-rating")[offset:limit]
    if review_data.count() != 0:
        return render(
            request,
            "movies/detail.html",
            {
                "movie": model,
                "total_rating": total_rating,
                "page_count": page_count - 1,
                "page_range": range(page_count),
                "review_data": review_data,
                "page": page,
            },
        )
    else:
        return redirect("/movies")


def movie_create(request):
    """
    create movie page definition
    """
    content = request.POST
    print(content)
    return render(request, "movies/create_page.html", {})
