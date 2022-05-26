from django.urls import path, include
from . import views

app_name = 'user'

urlpatterns = [
    path('user-info/', views.user_info, name='user_info'),
    # path('test/', views.testapi, name='test'),
]