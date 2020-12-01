from django.urls import path
from . import views as movie_views

app_name = "movies"

urlpatterns = [
    path("", movie_views.movie_main, name="main"),
    path("<int:pk>/", movie_views.movie_detail, name="detail"),
    path("create-form/", movie_views.movie_create, name="create"),
    path("create-progress/", movie_views.movie_create_progress, name="create_progress"),
]