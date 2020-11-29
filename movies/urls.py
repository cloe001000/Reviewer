from django.urls import path
from . import views as movie_views

app_name = "movies"

urlpatterns = [
    path("", movie_views.movie_main, name="main"),
    path("<int:pk>/", movie_views.movie_detail, name="detail"),
    path("create/", movie_views.movie_create, name="create"),
]