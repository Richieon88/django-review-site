from django.urls import path
from . import views
from django.shortcuts import render
from games.models import Game
from django.db.models import Avg

def homepage(request):
    latest_games = Game.objects.order_by('-release_date')[:5]
    top_rated_games = Game.objects.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')[:5]
    context = {
        'latest_games': latest_games,
        'top_rated_games': top_rated_games,
    }
    return render(request, 'index.html', context)


