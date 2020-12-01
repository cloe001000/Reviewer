from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import models as movie_model
from categories.models import MovieCategory
from people.models import Person
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
    try:
        page = int(request.GET.get("page", 0) or 0)
        # 일단은 리뷰 더보기 기능으로 생각
        model = movie_model.Movie.objects.get(pk=pk)
        total_rating = model.total_rating()
        reviews = model.review_set.all()
        page_size = 20
        main_page_size = 5
        page_count = int(
            (movie_model.Movie.objects.count() - main_page_size) / page_size
        )
        limit = (page * page_size) + main_page_size
        offset = limit - page_size if limit > main_page_size else 0
        review_data = reviews.order_by("-rating")[offset:limit]
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
    except movie_model.Movie.DoesNotExist:
        return redirect(reverse("movies:main"))


def movie_create(request):
    """
    create movie page definition
    """
    movie_categories = MovieCategory.objects.all()
    actores = Person.objects.filter(kind=Person.KIND_ACTOR)
    directores = Person.objects.filter(kind=Person.KIND_DIRECTOR)
    return render(
        request,
        "movies/create_page.html",
        {
            "movie_categories": movie_categories,
            "actores": actores,
            "directores": directores,
        },
    )


def movie_create_progress(request):
    content = dict(request.POST)
    INPUT_title = content.get("title")  # 모두다 LIST타입!!
    INPUT_plot = content.get("plot")
    INPUT_year = content.get("year")
    INPUT_add_actor = content.get("add_actor")
    INPUT_actor = content.get("actor")[1:]
    # form에서 actor의 default로 None하나가 설정되어있다 그것을 빼고 받아온다
    INPUT_director = content.get("director")
    INPUT_genre = content.get("genre")
    # ---------데이터 정리------------
    try:
        directors = Person.objects.filter(kind="director")
        director = directors.get(name=INPUT_director[0])
        genre = MovieCategory.objects.filter(genre=INPUT_genre[0])[0]
        title = INPUT_title[0]
        plot = INPUT_plot[0]
        year = int(INPUT_year[0])
    except (Person.DoesNotExist, ValueError):
        movie_categories = MovieCategory.objects.all()
        actores = Person.objects.filter(kind=Person.KIND_ACTOR)
        directores = Person.objects.filter(kind=Person.KIND_DIRECTOR)
        return render(
            request,
            "movies/create_page.html",
            {
                "movie_categories": movie_categories,
                "actores": actores,
                "directores": directores,
                "error": "True",
            },
        )
    else:
        movie_instanse = movie_model.Movie(
            title=title, plot=plot, genre=genre, year=year, director=director
        )
        movie_instanse.save()
        # Many To Many를 사용하려면 id가 필요하다 그래서 먼저 save()를 통해 자동 생성되게 해준다
        actors_queryset = Person.objects.filter(kind="actor")
        for name in INPUT_actor:
            filterset = actors_queryset.filter(name=name)
            for actor in filterset:
                movie_instanse.actor.add(actor)
        PK = movie_instanse.pk
        print(PK)
        return HttpResponseRedirect(reverse("movies:detail", args=(PK,)))
    # URL을 다룰때 value뺴고 다 str으로 생각해
