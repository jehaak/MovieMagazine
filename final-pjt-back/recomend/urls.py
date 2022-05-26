from django.urls import path, include
from . import views

app_name = 'recomend'

urlpatterns = [
    path('hotmovie/', views.hotmovie, name='hotmovie'),
]