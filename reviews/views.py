from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewForm
from games.models import Game
from games.views import game_detail

# Create your views here.
def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'reviews/review_detail.html', {'review': review})

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            game_id = form.cleaned_data['game_id']
            game = get_object_or_404(Game, pk=game_id)
            review = form.save(commit=False)
            review.game = game
            review.user = request.user
            review.save()
            return redirect('game_detail', pk=game_id)
    else:
        form = ReviewForm()
    
    return render(request, 'reviews/submit_review.html', {'form': form})
