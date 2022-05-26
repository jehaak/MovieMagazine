from dataclasses import field
from .models import Director, Actor, Movie
from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.models import UserLikeDirector, UserLikeActor, UserLikeMovies, UserWatchedMovies
from .models import Director, Actor, Movie

User = get_user_model()

#========================================================================
#========================================================================
# 영화카드 시리얼라이저
class MovieCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'local_id', 'poster_url', 'release_date', 'genre', 'popularity', 'id', 'overview',)

# 영화카드시리얼라이저 끝
#========================================================================
#========================================================================


#========================================================================
#========================================================================
# 배우프로필시리얼라이저 
class ActorProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('profile_url', 'name', 'popularity', 'id',)

# 배우카드 시리얼라이저 끝
#========================================================================
#========================================================================


#========================================================================
#========================================================================
# 감독프로필시리얼라이저
class DirectorProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = ('profile_url', 'name', 'popularity', 'id',)
# 감독카드 시리얼라이저 끝
#========================================================================
#========================================================================