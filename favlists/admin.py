from django.contrib import admin
from . import models

# 언더바가 뷰로 가면 알아서 띄어쓰기로 변한다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Register your models here.
@admin.register(models.FavList)
class FavListAdmin(admin.ModelAdmin):
    list_display = ("list_name", "created_by")
    list_filter = ("book", "movie")
    search_fields = ("created_by__username", "list_name")
    # 관계형 필드일 경우 대상 모델 안의 필드로 한단계더 들어가야 한다 이때 "__"연산자로 이어준다
    # 이것을 search필드라서 그렇다 무엇으로 검색할지 지정해야 하기 때문이다,list_display같은데는 그냥 불러주면 된다
    filter_horizontal = ("book", "movie")
    # 이것을 통해 admin내부에서 Many To MAny를 효율적으로 볼수 있다
