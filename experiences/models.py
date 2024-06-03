from django.db import models
from common.models import CommonModel


class Experience(CommonModel):
    """Experience Model Description"""

    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    name = models.CharField(
        max_length=250,
    )
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="experiences",
    )
    pet_friendly = models.BooleanField(
        default=True,
    )
    price = models.PositiveIntegerField()
    address = models.CharField(
        max_length=250,
    )
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField(
        "experiences.Perk",
        related_name="experiences",
    )
    category = models.ForeignKey(
        "categories.Category",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="experiences",
    )

    def __str__(self):
        return self.name

    def total_perks(self):
        return self.perks.count()

    def rating(experience):
        count = experience.reviews.count()
        if count == 0:
            return "No Reviews"
        else:
            total_rating = 0
            for review in experience.reviews.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 3)


class Perk(CommonModel):
    """What is included on an Experience"""

    name = models.CharField(
        max_length=100,
    )
    detail = models.CharField(
        max_length=250,
        blank=True,
        default="",
    )
    explanation = models.TextField(
        blank=True,
        default="",
    )

    def __str__(self):
        return self.name
