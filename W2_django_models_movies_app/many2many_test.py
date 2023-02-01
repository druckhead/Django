import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"
django.setup()

from movies_app.models import *

# m = Movie.objects.get(id=3)
# new_actor = Actor(name="ddddddd", birth_year=2000)
# new_actor.save()
# ma = MovieActor(movie=m, actor=new_actor, salary=1000000, main_role=False)
# ma.save()

# new_actor = Actor.objects.create(name="ppppp", birth_year=1988)
# new_actor.save()
# ma = MovieActor(movie_id=m.id, actor_id=new_actor.id, salary=1000000, main_role=False)
# ma.save()

# m.actors.create(
#     name="yyyyyy",
#     birth_year=2001,
#     through_defaults={"salary": 100000, "main_role": False},
# )

# m = Movie.objects.get(id=1)
# m.actors.add(
#     Actor.objects.get(id=3), through_defaults={"salary": 2500000, "main_role": False}
# )

# m = Movie.objects.get(id=3)
# a = Actor.objects.get(name__contains='ppp')
# m.actors.remove(a)
# a.delete()

# m = Movie.objects.get(id=3)
# print(m.actors.all())
# print(m.movieactor_set.all())

# a = Actor.objects.get(id=3)
# print(a.movie_set.all())
# a.movie_set.add(
#     Movie.objects.get(id=1), through_defaults={"salary": 150000, "main_role": False}
# )
