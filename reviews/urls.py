from django.urls import path
from . import views

urlpatterns = [
    path('review_list', views.review_list, name='review_list'),
    path('submit/', views.submit_review, name='submit_review'),
    path('<int:pk>/', views.review_detail, name='review_detail'),
    path('game/<int:pk>/', views.game_detail, name='game_detail'),
    path('profile/', views.profile, name='profile'),
    path('delete/<int:pk>/', views.delete_review, name='delete_review'),
]
