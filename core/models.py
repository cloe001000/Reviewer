from django.db import models

# 원하는 형식으로 datime받기 from django import forms 이후 forms.DateTimeField해서 필드 만들기
# https://hashcode.co.kr/questions/4222/django-datetimefield-%ED%8F%AC%EB%A7%B7-%EB%B3%80%EA%B2%BD-%EB%B0%A9%EB%B2%95
# Create your models here.


class TimeStampedModel(models.Model):

    """ TimeStampedModel Definition"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
