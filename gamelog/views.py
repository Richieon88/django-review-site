from django.urls import path
from . import views
from django.shortcuts import render
from games.models import Game
from django.db.models import Avg
from reviews.models import Review

def homepage(request):
    latest_reviews = Review.objects.order_by('-created_at')[:5]
    top_rated_games = Game.objects.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')[:5]
    context = {
        'latest_reviews': latest_reviews,
        'top_rated_games': top_rated_games,
    }
    return render(request, 'index.html', context)


