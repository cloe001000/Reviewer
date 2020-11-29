from django.urls import path
from . import views as book_views

app_name = "books"

urlpatterns = [
    path("", book_views.book_main, name="main"),
    path("<int:pk>/", book_views.book_detail, name="detail"),
]