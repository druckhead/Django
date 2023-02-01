from datetime import datetime
from random import randint
import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"
django.setup()

from movies_app.models import Movie, Rating, Review

# new_movie = Movie(name="aaa", release_year=2020, duration_in_mins=124)
# new_movie.save()
# new_movie = Movie(name="bbb", release_year=2020, duration_in_mins=124)
# new_movie.save()
# new_movie = Movie(name="ccc", release_year=2020, duration_in_mins=124)
# new_movie.save()
# new_movie = Movie(name="ddd", release_year=2020, duration_in_mins=124)
# new_movie.save()

# all_movies = Movie.objects.all()
# total_duration = 0
# for movie in all_movies:
#     total_duration += movie.duration_in_mins

# print(total_duration)

# all_movies = Movie.objects.all()
# for movie in all_movies:
#     rating = Rating(movie=movie, rating=randint(0, 11), rating_date=datetime.now().date()).save()

# movie = Movie.objects.get(pk=3)
# print(movie.rating_set.all())

# all_movies = Movie.objects.all()
# for movie in all_movies:
#     review = Review(movie=movie, review_text="lorem" * randint(10, 20), review_date=datetime.now().date()).save()

# movie = Movie.objects.get(pk=3)
# print(movie)

# r = Rating.objects.get(pk=1)
# print(r.movie)

# movie = Movie.objects.get(pk=1)
# print(movie.rating_set.all())

# Movie.objects.all()
# Movie.objects.filter()
# m = Movie.objects.get(duration_in_mins=14)

# movies_qs = Movie.objects.all().values_list('name', 'duration_in_mins')
# # print(movies[0])
# print(movies_qs)
# movies_qs = movies_qs.filter(release_year__gt=2020)
# print(movies_qs.query)
# movies_qs = movies_qs[:2]
# print(movies_qs.query)

# m1 = Movie.objects.filter(release_year__gt=2020, duration_in_mins__lte=15)
# m2 = Movie.objects.filter(release_year__gt=2020).filter(duration_in_mins__lte=15)

# print(m1, m2)

# filter_by_year = 2020
# filter_by_min = None
# name_to_filter = "aaa"

# m = Movie.objects.all()
# if filter_by_year:
#     m = m.filter(release_year=filter_by_year)
# if filter_by_min:
#     m = m.filter(duration_in_mins=filter_by_min)
# if name_to_filter:
#     m = m.filter(name__iexact=name_to_filter)
    
# print(m.query)
