from django.shortcuts import render
from .models import Game
from reviews.models import Review
from django.db.models import Avg

# Create your views here.
def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/games_list.html', {'games': games})

def game_detail(request, pk):
    game = Game.objects.get(pk=pk)
    return render(request, 'games/game_detail.html', {'game': game})

def homepage(request):
    latest_games = Game.objects.order_by('-release_date')[:5]
    top_rated_games = Game.objects.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')[:5]
    context = {
        'latest_games': latest_games,
        'top_rated_games': top_rated_games,
    }
    return render(request, 'index.html', context)
