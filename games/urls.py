from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('game_list/', views.game_list, name='game_list'),
    path('<int:pk>/', views.game_detail, name='game_detail'),
    path('add_review/<int:pk>/', views.add_review, name='add_review'),
]