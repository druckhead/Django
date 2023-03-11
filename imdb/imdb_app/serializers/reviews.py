from django.contrib.auth.models import User
from rest_framework import serializers

from imdb_app.models import Movie, Review


class ReviewSerializer(serializers.ModelSerializer):
    movie_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()
    

    class Meta:
        model = Review
        fields = '__all__'

    def get_movie_name(self, obj):
        movie = Movie.objects.get(pk=obj.movie.id)
        return movie.name

    def get_full_name(self, obj):
        user = User.objects.get(pk=obj.user.id)
        return f"{user.first_name} {user.last_name}"
