from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import UserWatchedMovies, Movie
from .models import UserWatchedMovies
from movies.views import moviecard
from .serializers import UserInfoSerializer
from recomend.views import byactor, bydirector

User = get_user_model()
# Create your views here.


@api_view(['GET'])
def user_info(request):
    movie = Movie.objects.get(id=43)
    print(UserWatchedMovies.objects.filter(user_watched_movies=request.user, movie_watched_users=movie))
    if request.user.is_authenticated:
        user = request.user
        result = {}
        result['by_actor_recomend'] = byactor(user)
        result['by_director_recomend'] = bydirector(user)
        serializer = UserInfoSerializer(user)
        result['user_data'] = serializer.data
        # 유저가 본 영화목록 추가
        watched_movies = UserWatchedMovies.objects.filter(user_watched_movies=user.id)
        movies_id = []
        print('유저인포 요청')
        for movie in watched_movies:
            movies_id.append(movie.movie_watched_users.id)
        print(movies_id)
        result['user_watched'] = moviecard(movies_id, user)
        return Response(result)
    return Response('로그인필요')


# @login_required
# @api_view(['GET', 'POST'])
# def testapi(request):
#     req = request.data
#     print(req['card_num'])