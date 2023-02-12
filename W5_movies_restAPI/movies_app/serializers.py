from rest_framework import serializers
from rest_framework.fields import CharField, IntegerField
from .models import *


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ["actors", "description"]
        depth = 1


class MovieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ["actors"]


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class ActorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["name"]


class MyActorSerializer(serializers.Serializer):
    id = IntegerField(read_only=True)
    name = CharField(
        max_length=256,
        min_length=3,
        allow_blank=False,
        trim_whitespace=True,
    )
    birth_year = IntegerField(
        max_value=2020,
        min_value=1900,
    )

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass


class MovieActorSerializer(serializers.ModelSerializer):
    # actor = serializers.StringRelatedField(many=False)

    class Meta:
        model = MovieActor
        exclude = ["movie"]
        depth = 1


class WritableMovieActorRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Actor.objects.all()

    def to_internal_value(self, data):
        val = super().to_internal_value(data)
        return val.pk


class AddMovieActorSerializer(serializers.Serializer):
    # actor_id = WritableMovieActorRelatedField(read_only=False, many=False)
    actor_id = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all().values_list("id", flat=True)
    )
    salary = serializers.IntegerField(min_value=0)
    main_role = serializers.BooleanField()

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def create(self, validated_data):
        MovieActor.objects.create(movie_id=self.context["movie_id"], **validated_data)
