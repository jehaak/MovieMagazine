from django.urls import path, include
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_db, name='create'),
    path('movielist/', views.movielist, name='movielist'),
    path('like/<int:movie_id>/', views.movielike, name='movielike'),
    path('watched/<int:movie_id>/', views.moviewatched, name='moviewatched'),
    path('actor/<int:actor_id>/', views.actor_profile, name='actor_profile'),
    path('director/<int:director_id>/', views.director_profile, name='director_profile'),
    path('detail/<int:movie_id>/', views.movie_detail, name='movie_detail'),
]