from django.urls import path, include
from . import views

app_name = 'search'

urlpatterns = [
    path('<keyword>', views.search, name='search'),
    path('<keyword>', views.search2, name='search'),
    path('auto/', views.autosearch, name='autosearch')    
]