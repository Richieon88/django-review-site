from django.urls import path
from . import views
from games.views import game_detail 

urlpatterns = [
    path('review_list/', views.review_list, name='review_list'),
    path('submit/', views.submit_review, name='submit_review'),
    path('reviews/<int:pk>/', views.review_detail, name='review_detail'),
    path('game/<int:pk>/', game_detail, name='game_detail'),
    path('profile/', views.profile, name='profile'),
    path('delete/<int:pk>/', views.delete_review, name='delete_review'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('like_comment/', views.like_comment, name='like_comment'),
]
