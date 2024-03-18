from django.shortcuts import render
from .models import Game

# Create your views here.
def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/games_list.html', {'games': games})

def game_detail(request, pk):
    game = Game.objects.get(pk=pk)
    return render(request, 'games/game_detail.html', {'game': game})
