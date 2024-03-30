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
    game = get_object_or_404(Game, pk=pk)
    avg_rating = game.reviews.aggregate(Avg('rating'))['rating__avg']
    context = {
        'game': game,
        'avg_rating': avg_rating,
    }
    return render(request, 'games/game_detail.html', context)


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
            return redirect('games:game_detail', pk=pk)
    else:
        form = ReviewForm()

    context = {'form': form, 'game': game}
    return render(request, 'reviews/add_review.html', context)
