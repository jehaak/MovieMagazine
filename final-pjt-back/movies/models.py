from django.db import models
from django.forms import CharField

class Director(models.Model):
    name = models.CharField(max_length=100)
    gender = models.IntegerField(null=True)
    local_id = models.IntegerField(null=True)
    popularity = models.FloatField(null=True)
    profile_url = models.TextField(null=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100)
    gender = models.IntegerField(null=True)
    local_id = models.IntegerField(null=True)
    popularity = models.FloatField(null=True)
    profile_url = models.TextField(null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor, related_name='movies')
    local_id = models.IntegerField()
    popularity = models.FloatField(null=True)
    score = models.FloatField()
    title = models.CharField(max_length=10000)
    audience = models.IntegerField()
    release_date = models.IntegerField()
    genre = models.CharField(max_length=10000)
    poster_url = models.TextField()
    overview = models.TextField()

    def __str__(self):
        return self.title


