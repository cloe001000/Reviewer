from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# abscractuser처럼 admin도 더 기능이 있는걸 베이스로 사용한다(검색창,비번바꾸는form등등)

# 장고가 모델을 이용해서 admin Form을 만들어줄수 있게된다. 모델에게 "필요한 데이터"를 요청해서 form을 만든다
# 데코레이터 인자로 admin클래스가 넘어가고 데코레이터 매개변수로 models.User가 넘어간다 그리고 들어가서 융합된다
@admin.register(models.User)  # === admin.site.register(models.User, CustomUserAdmin)
class CustomUserAdmin(UserAdmin):  # 데코레이터가 models.User를 받아서 이 클래스로 그것을 컨트롤 한다
    """ Custom User Admin"""

    Custom_fieldsets = (  # level_1 단위 = 튜플에 필드셋이름,딕셔너리
        (
            "Profile",
            {
                "fields": (
                    "username",
                    "bio",
                    "preference",
                    "language",
                    "email",
                    "is_staff",
                    "is_active",
                    "date_joined",
                )
            },
        ),
        (
            "Preferred genre",
            {
                "fields": (
                    "Book_Genre",
                    "Movie_Genre",
                ),
            },
        ),
    )
    # fieldsets이 덮어쓰여지면서 기존것들이 다 사라지므로 이렇게 더해줄수 있다
    fieldsets = Custom_fieldsets

    list_display = (
        "username",
        "preference",
        "Book_Genre",
        "Movie_Genre",
        "email",
        "language",
        "is_staff",
        "is_superuser",
    )

    list_filter = ("preference", "language", "Book_Genre", "Movie_Genre")
