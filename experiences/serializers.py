from rest_framework.serializers import ModelSerializer
from .models import Perk, Experience
from categories.serializers import CategorySerializer
from users.serializers import TinyUserSerializer


class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"


class ExperienceSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    perks = PerkSerializer(read_only=True, many=True)
    host = TinyUserSerializer(read_only=True)

    class Meta:
        model = Experience
        fields = "__all__"
