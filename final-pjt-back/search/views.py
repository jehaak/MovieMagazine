from platform import architecture
from rest_framework.decorators import api_view
from movies.models import Actor, Director, Movie
from rest_framework.response import Response
from movies.views import moviecard, actorcard, directorcard, director_profile_maker, actor_profile_maker, movie_detail_maker
from django.db.models import Q

# Create your views here.


@api_view(['POST'])
def autosearch(request):
    keyword = request.data['keyword']
    print(keyword)
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    result = []
    actors = Actor.objects.filter(name__contains=keyword)
    for actor in actors:
        result.append([actor.name, len(actor.name)])

    directors = Director.objects.filter(name__contains=keyword)
    for director in directors:
        result.append([director.name, len(director.name)])

    movies = Movie.objects.filter(title__contains=keyword)
    for movie in movies:
        result.append([movie.title, len(movie.title)])

    result.sort(key=lambda x : x[1])
    length = len(result)
    real_result = []
    for i in range(5):
        if i < length:
            real_result.append(result[i][0])
    return Response(real_result)


@api_view(['POST'])
def search2(request, keyword):
    print(keyword)
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    result = {
        'perfect': {
            'actor': [],
            'director': [],
            'movie': [],
        },
        'director': [],
        'actor': [],
        'movie': []
    }
    # 완전 일치하는거 체크
    if Actor.objects.filter(name=keyword).exists():
        actors = Actor.objects.filter(name=keyword)
        for actor in actors:
            result['perfect']['actor'].append(actor_profile_maker(user, actor.id))
    if Director.objects.filter(name=keyword).exists():
        directors = Director.objects.filter(name=keyword)
        for director in directors:
            result['perfect']['director'].append(director_profile_maker(user, director.id))
    if Movie.objects.filter(title=keyword).exists():
        movies = Movie.objects.filter(title=keyword)
        for movie in movies:
            result['perfect']['movie'].append(movie_detail_maker(user, movie.id))
    
    # 단어 포함되어있는지 체크
    actors = Actor.objects.filter(~Q(name=keyword) & Q(name__contains=keyword))
    actors_id = []
    for actor in actors:
        actors_id.append(actor.id)
    result['actor'] = actorcard(actors_id)

    directors = Director.objects.filter(~Q(name=keyword) & Q(name__contains=keyword))
    directors_id = []
    for director in directors:
        directors_id.append(director.id)
    result['director'] = directorcard(directors_id)

    movies = Movie.objects.filter((~Q(title=keyword) & Q(title__contains=keyword)))
    movies_id = []
    for movie in movies:
        movies_id.append(movie.id)
    result['movie'] = moviecard(movies_id, user)

    return Response(result)



@api_view(['POST'])
def search(request, keyword):
    # is_enter = request.data['is_enter'] 
    # keyword = request.data['keyword']
    # print(keyword)
    # if is_enter == 'true':
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    result = {
        'perfect': {
            'actor': [],
            'director': [],
            'movie': [],
        },
        'director': [],
        'actor': [],
        'movie': []
    }
    # 완전 일치하는거 체크
    if Actor.objects.filter(name=keyword).exists():
        actors = Actor.objects.filter(name=keyword)
        for actor in actors:
            result['perfect']['actor'].append(actor_profile_maker(user, actor.id))
    if Director.objects.filter(name=keyword).exists():
        directors = Director.objects.filter(name=keyword)
        for director in directors:
            result['perfect']['director'].append(director_profile_maker(user, director.id))
    if Movie.objects.filter(title=keyword).exists():
        movies = Movie.objects.filter(title=keyword)
        for movie in movies:
            result['perfect']['movie'].append(movie_detail_maker(user, movie.id))
    
    # 단어 포함되어있는지 체크
    actors = Actor.objects.filter(~Q(name=keyword) & Q(name__contains=keyword))
    actors_id = []
    for actor in actors:
        actors_id.append(actor.id)
    result['actor'] = actorcard(actors_id)

    directors = Director.objects.filter(~Q(name=keyword) & Q(name__contains=keyword))
    directors_id = []
    for director in directors:
        directors_id.append(director.id)
    result['director'] = directorcard(directors_id)

    movies = Movie.objects.filter((~Q(title=keyword) & Q(title__contains=keyword)))
    movies_id = []
    for movie in movies:
        movies_id.append(movie.id)
    result['movie'] = moviecard(movies_id, user)

    return Response(result)

    # 앤터 아니고 input이면
    result = []
    actors = Actor.objects.filter(name__contains=keyword)
    for actor in actors:
        result.append([actor.name, len(actor.name)])

    directors = Director.objects.filter(name__contains=keyword)
    for director in directors:
        result.append([director.name, len(director.name)])

    movies = Movie.objects.filter(title__contains=keyword)
    for movie in movies:
        result.append([movie.title, len(movie.title)])

    result.sort(key=lambda x : x[1])
    length = len(result)
    real_result = []
    for i in range(5):
        if i < length:
            real_result.append(result[i][0])
    return Response(real_result)