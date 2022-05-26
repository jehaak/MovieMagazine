from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from .models import Actor, Director, Movie
from accounts.models import UserLikeMovies, UserWatchedMovies, UserLikeDirector, UserLikeActor
from rest_framework.response import Response
from .serializers import MovieCardSerializer, DirectorProfileSerializer, ActorProfileSerializer
import requests
import json
from recomend.views import byactor, bydirector, hotmovie


def movielist(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@api_view(['GET'])
def home(request):
    print('홈 요청')
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    result = {}
    result['recent_movie'] = recent_movie(user)
    if user:
        result['by_actor_recomend'] = byactor(user)
        result['by_director_recomend'] = bydirector(user)
    else:
        result['by_actor_recomend'] = 'not_login'
        result['by_director_recomend'] = 'not_login'
    result['hot_movie'] = hotmovie(user)

    return Response(result)


def recent_movie(user):
    movies_id = []
    movies = Movie.objects.order_by('-release_date')[:6]
    for movie in movies:
        movies_id.append(movie.id)
    return moviecard(movies_id, user)


@api_view(['POST'])
def movielike(request, movie_id):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    result = 1
    print('==================================')
    print(request.user.username)
    movie = Movie.objects.get(local_id=movie_id)
    checkinstance = UserLikeMovies.objects.filter(user_like_movies=request.user, movie_like_users=movie)
    # 이 유저가 좋아요를 눌렸었으면:
    if checkinstance.count():
        result = 0
        # 좋아요 제거
        checkinstance.delete()
        # 감독, 배우 정보 가져오기
        director = Director.objects.get(id=movie.director_id)
        actors = movie.actors.all()

        # 감독, 유저관계 수정
        userlikedirector = UserLikeDirector.objects.get(user=request.user, director=director)
        userlikedirector.level = userlikedirector.level-1
        userlikedirector.save()

        # 감독, 배우관계 수정
        for actor in actors:
            userlikeactor = UserLikeActor.objects.get(user=request.user, actor=actor)
            userlikeactor.level = userlikeactor.level-1
            userlikeactor.save()

        T_or_F = 'false'

    # 안눌렸었으면:
    else:
        # 좋아요 추가
        UserLikeMovies.objects.create(user_like_movies=request.user, movie_like_users=movie)
        
        # 감독, 배우 정보 가져오기
        director = Director.objects.get(id=movie.director_id)
        actors = movie.actors.all()
        
        # 감독, 유저관계 수정
        userlikedirector = UserLikeDirector.objects.filter(user=request.user, director=director)
        # 이미 관계가 있으면:
        if userlikedirector.count():
            userlikedirector = UserLikeDirector.objects.get(user=request.user, director=director)
            userlikedirector.level = userlikedirector.level + 1
            userlikedirector.save()
        # 최초로 눌렸으면
        else:
            userlikedirector = UserLikeDirector.objects.create(user=request.user, director=director, level = 1)
        
        # 배우들, 유저 관계 수정
        for actor in actors:
            userlikeactor = UserLikeActor.objects.filter(user=request.user, actor=actor)
            # 이미 관계가 있으면:
            if userlikeactor.count():
                userlikeactor = UserLikeActor.objects.get(user=request.user, actor=actor)
                userlikeactor.level = userlikeactor.level + 1
                userlikeactor.save()
            # 최초로 눌렸으면
            else:
                userlikeactor = UserLikeActor.objects.create(user=request.user, actor=actor, level = 1)
        T_or_F = 'true'

    # 순위정하기
    # -1이 아닌 필드들 감독id 들고옴
    user = request.user
    directors = UserLikeDirector.objects.filter(user=user).order_by('-level')
    print(len(directors))
    if len(directors) >= 1:
        user.first_director_id = directors[0].director_id
        user.save()
    if len(directors) >= 2:
        user.second_director_id = directors[1].director_id
        user.save()
    if len(directors) >= 3:
        user.third_director_id = directors[2].director_id
        user.save()
    
    # -1이 아닌 필드들 배우id 들고옴
    user = request.user
    actors = UserLikeActor.objects.filter(user=user).order_by('-level')
    print(len(actors))
    if len(actors) >= 1:
        user.first_actor_id = actors[0].actor_id
        user.save()
    if len(actors) >= 2:
        user.second_actor_id = actors[1].actor_id
        user.save()
    if len(actors) >= 3:
        user.third_actor_id = actors[2].actor_id
        user.save()
    return Response(result)
    # return redirect('user:user_info')


@api_view(['POST'])
def moviewatched(request, movie_id):
    result = 0
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    movie = Movie.objects.get(local_id=movie_id)
    checkinstance = UserWatchedMovies.objects.filter(user_watched_movies=request.user, movie_watched_users=movie)
    # 이 유저가 봤어요를 눌렸었으면:
    if checkinstance.count():
        # 봤어요 제거
        checkinstance.delete()
        result = 0
        return Response(result)
        # return redirect('user:user_info')
    
    # 안눌렸었으면:
    else:
        # 봤어요 추가
        UserWatchedMovies.objects.create(user_watched_movies=request.user, movie_watched_users=movie)
        result = 1
        return Response(result)
        # return redirect('user:user_info')


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


def actorcard(actorid_list):
    result = []
    for actor_id in actorid_list:
        actor = Actor.objects.get(id=actor_id)
        serializer = ActorProfileSerializer(actor)
        result.append(serializer.data)
    return result


def directorcard(directorid_list):
    result = []
    for director_id in directorid_list:
        director = Director.objects.get(id=director_id)
        serializer = DirectorProfileSerializer(director)
        result.append(serializer.data)
    return result


def actor_profile_maker(user, actor_id):
    actor = Actor.objects.get(id=actor_id)
    # 유저, 배우 관계가 존재하면 쭉 진행하고, 없으면 만들어주기
    if user:
        if UserLikeActor.objects.filter(actor=actor, user=user).exists():
            pass
        else:
            UserLikeActor.objects.create(actor=actor, user=user, level=0)
    result = {}
    if user:
        result['actor_level'] = UserLikeActor.objects.get(actor=actor, user=user).level / Movie.objects.filter(actors=actor).count() *100
    else:
        result['actor_level'] = 'not_login'
    serializer = ActorProfileSerializer(actor)
    result['actor_info'] = serializer.data
    # 배우가 출연한 영화목록 추가
    casted_movies = Movie.objects.filter(actors=actor)
    movies_id = []
    for movie in casted_movies:
        movies_id.append(movie.id)
    result['casted_movies'] = moviecard(movies_id, user)

    # 이 배우 추천영화
    result['recomend_movie'] = 'no_movie'
    if user:
        tot_movies = Movie.objects.filter(actors=actor).order_by('-popularity')
        tot_num = len(tot_movies)
        level = UserLikeActor.objects.get(user=user, actor=actor).level
        idx = int(level)%tot_num
        initial_idx = idx
        # 전체 영화길이만큼 돌면서 안본영화 추천
        while len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies[idx].id))):
            idx = (idx+1)%tot_num
            if idx == initial_idx:
                result['recomend_movie'] = 'no_movie'
                break
        if tot_num == 1 and not len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies[idx].id))):
            result['recomend_movie'] = moviecard([tot_movies[idx].id], user)[0]
        if not len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies[idx].id))):
            result['recomend_movie'] = moviecard([tot_movies[idx].id], user)[0]
    return result


def director_profile_maker(user, director_id):
    director = Director.objects.get(id=director_id)
    if user:
        # 유저, 배우 관계가 존재하면 쭉 진행하고, 없으면 만들어주기
        if UserLikeDirector.objects.filter(director=director, user=user).exists():
            pass
        else:
            UserLikeDirector.objects.create(director=director, user=user, level=0)
    result = {}
    if user:
        result['director_level'] = UserLikeDirector.objects.get(director=director, user=user).level / Movie.objects.filter(director=director).count() *100
    else:
        result['director_level'] = 'not_login'
    serializer = DirectorProfileSerializer(director)
    result['director_info'] = serializer.data
    # 감독이 촬영한 영화목록 추가
    directed_movies = Movie.objects.filter(director=director)
    movies_id = []
    for movie in directed_movies:
        movies_id.append(movie.id)
    result['directed_movies'] = moviecard(movies_id, user)

    # 이 감독 추천 영화
    result['recomend_movie'] = 'no_movie'
    if user:
        tot_movies = Movie.objects.filter(director=director).order_by('-popularity')
        tot_num = len(tot_movies)
        level = UserLikeDirector.objects.get(user=user, director=director).level
        idx = int(level)%tot_num
        initial_idx = idx
        # 전체 영화길이만큼 돌면서 안본영화 추천
        while len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies[idx].id))):
            idx = (idx+1)%tot_num
            if idx == initial_idx:
                result['recomend_movie'] = 'no_movie'
                break
        if tot_num == 1 and not len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies[idx].id))):
            result['recomend_movie'] = moviecard([tot_movies[idx].id], user)[0]
        if not len(UserWatchedMovies.objects.filter(user_watched_movies=user, movie_watched_users=Movie.objects.get(id=tot_movies[idx].id))):
            result['recomend_movie'] = moviecard([tot_movies[idx].id], user)[0]
    return result


def movie_detail_maker(user, movie_id):
    movie = Movie.objects.get(id=movie_id)
    actors = movie.actors.all()
    actors_id = []
    for actor in actors:
        actors_id.append(actor.id)
    result = {}
    result['movie_info'] = moviecard([movie_id], user)
    result['director'] = directorcard([movie.director.id])
    result['actor'] = actorcard(actors_id)
    return result


# @login_required
@api_view(['GET'])
def actor_profile(request, actor_id):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    result = actor_profile_maker(user, actor_id)
    return Response(result)


# @login_required
@api_view(['GET'])
def director_profile(request, director_id):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    result = director_profile_maker(user, director_id)
    return Response(result)


# @login_required
@api_view(['GET'])
def movie_detail(request, movie_id):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    result = movie_detail_maker(user, movie_id)
    return Response(result)


# Create your views here.
# API에서 영화 들고오는 함수
# 리스트 안의 딕셔너리 형태
def get_movies():
    try: # 영화가 '존재'할 경우
        BASE_URL = 'https://api.themoviedb.org/3'
        path = '/movie/popular'
        result = [] # 반환 리스트
        for i in range(1, 100): # 페이지가 여러개일 경우 나올 수 있는 경우 다 출력
            recom_params={
                'api_key': 'b70a7f4bf007d7d4d9f3c02f5531f24d',
                'region': 'KR',
                'language': 'ko',
                'page': i,
            }
            # 위의 변수들을 통해 해당 영화 id값에 대응하는 '추천 영화 페이지' 반환
            recom = requests.get(BASE_URL+path, params=recom_params).json()
            result += recom['results']
        return result
    except IndexError: # 영화 없음
        return


# 영화 id로 크래딧 들고오는 함수
# {'cast': dict, 'crew': dict} 형태
def credits(id): 
    BASE_URL = 'https://api.themoviedb.org/3'
    try:
        recom_path = f'/movie/{id}/credits'
        recom_params={
            'api_key': 'b70a7f4bf007d7d4d9f3c02f5531f24d',
            'language': 'ko',
            }
            # 위의 변수들을 통해 해당 영화 id값에 대응하는 크레딧 페이지 반환
        credit = requests.get(BASE_URL+recom_path, params=recom_params).json()
        
        # 배우들 id 리스트에 넣어서 반환
        actor_list = []
        actor_id_list = []
        for actor in credit['cast']:
            actor_list.append(actor)
            actor_id_list.append(actor['id'])
        # 감독정보 찾아서 반환
        for crew in credit['crew']:
            if crew["department"] == 'Directing':
                return  actor_id_list, crew['id'], {'cast': actor_list, 'crew': crew}
    except:
        return [], {'cast': [], 'crew': {}}


# 장르 아이디로 장르 들고오는 함수
# 'genre1 genre2 genre3' 같은 문자열 형태
def get_genre(genre_ids):
    try:
        base_URL = 'https://api.themoviedb.org/3'
        path = '/genre/movie/list'
        params = {
        'api_key': 'b70a7f4bf007d7d4d9f3c02f5531f24d',
        'language': 'Ko',
        }
        response = requests.get(base_URL + path, params = params).json()
        result = ''
        for genre_id in genre_ids:
            for genre in response['genres']:
                if genre['id'] == genre_id:
                    result = result + genre['name'] + ' '
                    break
        result = result.rstrip()
        
        return result
    except:
        return ''


def create_db(response):
    # 최초 1회 실행. raw_moviedata, raw_creditdata, raw_genredata 생성
    movies = get_movies()
    cast_dir_list = []
    genre_dir = []
    for movie in movies:
        actors_id, director_id, credits_info = credits(movie['id'])
        cast_dir_list.append(credits_info)
        movie['actors_id'] = actors_id
        movie['director_id'] = director_id
        genre_dir.append(get_genre(movie['genre_ids']))

    with open('./raw_moviedata.json', 'w', encoding='utf-8') as file:
        json.dump(movies, file, ensure_ascii=False, indent=4)

    with open('./raw_creditdata.json', 'w', encoding='utf-8') as file:
        json.dump(cast_dir_list, file, ensure_ascii=False, indent=4)

    with open('./raw_genredata.json', 'w', encoding='utf-8') as file:
        json.dump(genre_dir, file, ensure_ascii=False, indent=4)


    # 저장해놓은 데이터 불러오기
    # raw_moviedata => movies
    # raw_creditdata => cast_dir_list
    # raw_genredata => genres
    with open('./raw_moviedata.json', 'r', encoding='utf-8') as file:
        movies = json.load(file)

    with open('./raw_creditdata.json', 'r', encoding='utf-8') as file:
        cast_dir_list = json.load(file)

    with open('./raw_genredata.json', 'r', encoding='utf-8') as file:
        genres = json.load(file)

    # 데이터베이스에 감독, 배우 추가하는 로직
    for cast_dir in cast_dir_list:

        # Actor 인스턴스 추가
        for actor in cast_dir['cast']:
            if len(Actor.objects.filter(local_id=actor['id'])):
                pass
            else:
                instance = Actor()
                instance.name = actor['name']
                instance.gender = actor['gender']
                instance.local_id = actor['id']
                instance.popularity = actor['popularity']
                instance.profile_url = actor['profile_path']
                # 더 추가해 넣어야함
                instance.save()
        
        # Director 인스턴스 추가
        instance = Director()
        if len(Director.objects.filter(local_id=cast_dir['crew']['id'])):
                pass
        else:
            instance.name = cast_dir['crew']['name']
            instance.gender = cast_dir['crew']['gender']
            instance.local_id = cast_dir['crew']['id']
            instance.popularity = cast_dir['crew']['popularity']
            instance.profile_url = cast_dir['crew']['profile_path']
            instance.save()

    # 데이터베이스에 영화 추가하는 로직
    for movie, genre in zip(movies, genres):
        if len(Movie.objects.filter(local_id=movie['id'])):
            pass
        else:
            # Movie 인스턴스 추가
            instance = Movie()
            director = Director.objects.get(local_id=movie['director_id'])
            instance.director = director
            instance.title = movie['title']
            instance.overview = movie['overview'] 
            instance.popularity = movie['popularity']
            instance.score = movie['vote_average']
            instance.audience = movie['vote_count']
            release_date = int(movie['release_date'].replace('-', ''))
            instance.release_date = release_date
            instance.poster_url = movie['poster_path']
            instance.local_id = movie['id']
            instance.genre = genre
            instance.save()
            # 영화별 배우 추가
            for actor_id in movie['actors_id']:
                actor = Actor.objects.get(local_id=actor_id)
                instance.actors.add(actor)

    return redirect('movies:movielist')

