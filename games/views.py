from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Game
from reviews.models import Review
from django.db.models import Avg
from reviews.forms import ReviewForm

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

@login_required
def add_review(request, pk):
    game = get_object_or_404(Game, pk=pk)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.game = game
            review.user = request.user
            review.save()
            return redirect('game_detail', pk=pk)
    else:
        form = ReviewForm()
    
    return render(request, 'reviews/add_review.html', {'form': form, 'game': game})