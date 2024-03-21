from django.shortcuts import render
from .models import Game

# Create your views here.
def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/games_list.html', {'games': games})

def game_detail(request, pk):
    game = Game.objects.get(pk=pk)
    return render(request, 'games/game_detail.html', {'game': game})

def homepage(request):
    latest_games = Game.objects.order_by('-release_date')[:3]  # Get latest 3 games
    top_rated_games = Game.objects.order_by('-rating')[:3]    # Get top rated 3 games
    context = {
        'latest_games': latest_games,
        'top_rated_games': top_rated_games,
    }
    return render(request, 'index.html', context)
