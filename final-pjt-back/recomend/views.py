from accounts.models import UserLikeMovies, UserWatchedMovies, UserLikeDirector, UserLikeActor
from movies.models import Actor, Director, Movie
from movies.serializers import MovieCardSerializer, DirectorProfileSerializer, ActorProfileSerializer
# 알고리즘 모듈
from datetime import datetime, timedelta
from collections import Counter


# Create your views here.

def directorcard(directorid_list):
    result = []
    for director_id in directorid_list:
        director = Director.objects.get(id=director_id)
        serializer = DirectorProfileSerializer(director)
        result.append(serializer.data)
    return result


def actorcard(actorid_list):
    result = []
    for actor_id in actorid_list:
        actor = Actor.objects.get(id=actor_id)
        serializer = ActorProfileSerializer(actor)
        result.append(serializer.data)
    return result


def bydirector(user):
    print('감독추천')
    result = { 'first_director': 'no_movie', 'second_director': 'no_movie', 'third_director': 'no_movie', 'first_director_info': 'no_director', 'second_director_info': 'no_director', 'third_director_info': 'no_director', 'first_director_level': 'no_director', 'second_director_level': 'no_director', 'third_director_level': 'no_director'}
    if user.first_director_id != -1:
        director1 = Director.objects.get(id=user.first_director_id)
        tot_movies_1 = Movie.objects.filter(director=director1).order_by('-popularity')
        tot_num1 = len(tot_movies_1)
        level = UserLikeDirector.objects.get(user=user, director=director1).level

        idx = int(level)%tot_num1
        initial_idx = idx
        # 전체 영화길이만큼 돌면서 안본영화 추천
        while len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies_1[idx].id))):
            idx = (idx+1)%tot_num1
            if idx == initial_idx:
                result['first_director'] = 'no_movie'
                break
        result['first_director_info'] = directorcard([user.first_director_id])[0]
        result['first_director_level'] = level/tot_num1*100
        if tot_num1 == 1 and not len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies_1[idx].id))):
            result['first_director'] = moviecard([tot_movies_1[idx].id], user)[0]
            
        if not len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies_1[idx].id))):
            result['first_director'] = moviecard([tot_movies_1[idx].id], user)[0]

    if user.second_director_id != -1:
        director2 = Director.objects.get(id=user.second_director_id)
        tot_movies_2 = Movie.objects.filter(director=director2).order_by('-popularity')
        tot_num2 = len(tot_movies_2)
        level = UserLikeDirector.objects.get(user=user, director=director2).level
        idx = int(level)%tot_num2
        initial_idx = idx
        # 전체 영화길이만큼 돌면서 안본영화 추천
        while len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies_2[idx].id))):
            idx = (idx+1)%tot_num2
            if idx == initial_idx:
                result['second_director'] = 'no_movie'
                break
        result['second_director_info'] = directorcard([user.second_director_id])[0]
        result['second_director_level'] = level/tot_num2*100
        if tot_num2 == 1 and not len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies_2[idx].id))):
            result['second_director'] = moviecard([tot_movies_2[idx].id], user)[0]
        if not len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies_2[idx].id))):
            result['second_director'] = moviecard([tot_movies_2[idx].id], user)[0]
    
    if user.third_director_id != -1:
        director3 = Director.objects.get(id=user.third_director_id)

        tot_movies_3 = Movie.objects.filter(director=director3).order_by('-popularity')
        tot_num3 = len(tot_movies_3)
        level = UserLikeDirector.objects.get(user=user, director=director3).level
        idx = int(level)%tot_num3
        initial_idx = idx
        # 전체 영화길이만큼 돌면서 안본영화 추천
        print(len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies_3[idx].id))))
        while len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies_3[idx].id))):
            idx = (idx+1)%tot_num3
            if idx == initial_idx:
                result['third_director'] = 'no_movie'
                break
        result['third_director_info'] = directorcard([user.third_director_id])[0]
        result['third_director_level'] = level/tot_num3*100
        if tot_num3 == 1 and not len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies_3[idx].id))):
            result['third_director'] = moviecard([tot_movies_3[idx].id], user)[0]
        if not len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies_3[idx].id))):
            result['third_director'] = moviecard([tot_movies_3[idx].id], user)[0]
    return result


def byactor(user):
    print('배우추천')
    result = { 'first_actor': 'no_movie', 'second_actor': 'no_movie', 'third_actor': 'no_movie', 'first_actor_info': 'no_actor', 'second_actor_info': 'no_actor', 'third_actor_info': 'no_actor', 'first_actor_level': 'no_actor', 'second_actor_level': 'no_actor', 'third_actor_level': 'no_actor'}
    showed = []
    if user.first_actor_id != -1:
        actor1 = Actor.objects.get(id=user.first_actor_id)
        tot_movies_1 = Movie.objects.filter(actors=actor1).order_by('-popularity')
        tot_num1 = len(tot_movies_1)
        level = UserLikeActor.objects.get(user=user, actor=actor1).level
        idx = int(level)%tot_num1
        initial_idx = idx
        # 전체 영화길이만큼 돌면서 안본영화 추천
        for i in range(tot_num1):
            if len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies_1[idx].id))) or (tot_movies_1[idx].id in showed):
                idx = (idx+1)%tot_num1
            else:
                break
        result['first_actor_info'] = actorcard([user.first_actor_id])[0]
        result['first_actor_level'] = level/tot_num1*100
        if tot_num1 == 1 and not len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies_1[idx].id))):
            id1 = tot_movies_1[idx].id
            result['first_actor'] = moviecard([id1], user)[0]
            showed.append(id1)
        if not len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies_1[idx].id))):
            id1 = tot_movies_1[idx].id
            result['first_actor'] = moviecard([id1], user)[0]
            showed.append(id1)
    
    if user.second_actor_id != -1:
        actor2 = Actor.objects.get(id=user.second_actor_id)
        tot_movies_2 = Movie.objects.filter(actors=actor2).order_by('-popularity')
        tot_num2 = len(tot_movies_2)
        level = UserLikeActor.objects.get(user=user, actor=actor2).level
        idx = int(level)%tot_num2
        initial_idx = idx
        # 전체 영화길이만큼 돌면서 안본영화 추천
        for i in range(tot_num2):
            if len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies_2[idx].id))) or (tot_movies_2[idx].id in showed):
                idx = (idx+1)%tot_num2
            else:
                break
        result['second_actor_info'] = actorcard([user.second_actor_id])[0]
        result['second_actor_level'] = level/tot_num2*100
        if tot_num2 == 1 and not len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies_2[idx].id))):
            id2= tot_movies_2[idx].id
            if not (id2 in showed):
                result['second_actor'] = moviecard([id2], user)[0]
                showed.append(id2)
        if not len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies_2[idx].id))):
            id2= tot_movies_2[idx].id
            if not (id2 in showed):
                result['second_actor'] = moviecard([id2], user)[0]
                showed.append(id2)
    
    if user.third_actor_id != -1:
        actor3 = Actor.objects.get(id=user.third_actor_id)
        tot_movies_3 = Movie.objects.filter(actors=actor1).order_by('-popularity')
        tot_num3 = len(tot_movies_3)
        level = UserLikeActor.objects.get(user=user, actor=actor3).level
        idx = int(level)%tot_num3
        initial_idx = idx
        # 전체 영화길이만큼 돌면서 안본영화 추천
        for i in range(tot_num3):
            if len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies_3[idx].id))) or (tot_movies_3[idx].id in showed):
                idx = (idx+1)%tot_num3
            else:
                break
        result['third_actor_info'] = actorcard([user.third_actor_id])[0]
        result['third_actor_level'] = level/tot_num3*100
        if tot_num3 == 1 and not len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies_3[idx].id))):
            id3= tot_movies_3[idx].id
            if not (id3 in showed):
                result['third_actor'] = moviecard([id3], user)[0]
                showed.append(id3)
        if not len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies_3[idx].id))):
            id3= tot_movies_3[idx].id
            if not (id3 in showed):
                result['third_actor'] = moviecard([id3], user)[0]
                showed.append(id3)

            # result['third_actor'] = moviecard([tot_movies_3[idx].id])[0]
    return result


def hotmovie(user):
    like = UserLikeMovies.objects.all()
    if len(like) > 100:
        like = like[:100]
    like_movies_id = []
    for movie in like:
        update_time = movie.updated_at.replace(tzinfo=None)
        now_time = datetime.now()
        delta = timedelta(hours=24)
        if now_time - update_time < delta:
            like_movies_id.append(movie.movie_like_users.id)
    cnt = Counter(like_movies_id).most_common()
    if cnt:
        id = cnt[0][0]
        result = moviecard([id], user)
        result.append(cnt[0][1])
    else:
        result = 'no_hotmovie'
    return result


# 무비카드 시리얼라이저 만들어서 리턴해주는 함수
def moviecard(movieid_list, user):
    result = []
    for movie_id in movieid_list:
        if user:
            watched = 'true' if UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=movie_id).exists() else 'false'
            like = 'true' if UserLikeMovies.objects.filter(user_like_movies=user, movie_like_users=movie_id).exists() else 'false'
        else:
            watched = 'not_login'
            like = 'not_login'
        serializer = MovieCardSerializer(Movie.objects.get(id=movie_id))
        temp_result = {'watched': watched, 'like': like}
        
        for key in serializer.data:
            value = serializer.data[key]
            temp_result[key] = value
        result.append(temp_result)
    return result