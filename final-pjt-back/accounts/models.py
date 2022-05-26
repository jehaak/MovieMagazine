from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from movies.models import Movie, Director, Actor


class User(AbstractUser):
    favorite_director_id = models.IntegerField(default=-1)
    favorite_actor_id = models.IntegerField(default=-1)

    first_director_id =  models.IntegerField(default=-1)
    second_director_id =  models.IntegerField(default=-1)
    third_director_id =  models.IntegerField(default=-1)

    first_actor_id =  models.IntegerField(default=-1)
    second_actor_id =  models.IntegerField(default=-1)
    third_actor_id =  models.IntegerField(default=-1)

class UserLikeMovies(models.Model):
    user_like_movies = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_like')
    movie_like_users = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_like')
    updated_at = models.DateTimeField(auto_now=True)

class UserWatchedMovies(models.Model):
    user_watched_movies = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_watched')
    movie_watched_users = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_watched')
    updated_at = models.DateTimeField(auto_now=True)

class UserLikeDirector(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_direcor')
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    level = models.FloatField()

class UserLikeActor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_actor')
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    level = models.FloatField()