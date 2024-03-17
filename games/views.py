from django.shortcuts import render, get_object_or_404
from .models import Game

# Create your views here.
def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/games_list.html', {'games': games})

def game_detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'games/game_detail.html', {'game': game})
