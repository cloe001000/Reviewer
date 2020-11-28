from django.db import models
from core.models import TimeStampedModel

# Create your models here.


class Person(TimeStampedModel):
    KIND_ACTOR = "actor"
    KIND_DIRECTOR = "director"
    KIND_WRITER = "writer"
    KIND_CHOICES = (
        (KIND_ACTOR, "Actor"),
        (KIND_DIRECTOR, "Director"),
        (KIND_WRITER, "Writer"),
    )
    name = models.CharField(max_length=30)
    photo = models.ImageField(null=True, blank=True)
    kind = models.CharField(choices=KIND_CHOICES, max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "People"