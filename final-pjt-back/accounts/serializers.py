from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserLikeDirector, UserLikeActor, UserLikeMovies, UserWatchedMovies
from movies.models import Director, Actor, Movie


#========================================================================
#========================================================================
# 유저정보 시리얼라이저
class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username', 
            "favorite_director_id",
            "favorite_actor_id",
            "first_director_id",
            "second_director_id",
            "third_director_id",
            "first_actor_id",
            "second_actor_id",
            "third_actor_id",
            # "user_watched",
            )
# 유저정보 시리얼라이저 끝
#========================================================================
#========================================================================