from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Perk, Experience
from categories.serializers import CategorySerializer
from users.serializers import TinyUserSerializer
from medias.serializers import PhotoSerializer
from wishlists.models import Wishlist


class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"


class ExperienceSerializer(ModelSerializer):
    rating = serializers.SerializerMethodField()
    is_host = serializers.SerializerMethodField()
    photos = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Experience
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_host",
            "photos",
        )

    def get_rating(self, experience):
        return experience.rating()

    def get_is_host(self, experience):
        request = self.context["request"]
        return experience.host == request.user


class ExperienceDetailSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    perks = PerkSerializer(read_only=True, many=True)
    host = TinyUserSerializer(read_only=True)
    is_host = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    photos = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Experience
        fields = "__all__"

    def get_rating(self, experience):
        return experience.rating()

    def get_is_host(self, experience):
        request = self.context.get("request")
        if request:
            return experience.host == request.user
        return False

    def get_is_liked(self, experience):
        request = self.context.get("request")
        if request:
            if request.user.is_authenticated:
                return Wishlist.objects.filter(
                    user=request.user,
                    experiences__id=experience.pk,
                ).exists()
            return False
