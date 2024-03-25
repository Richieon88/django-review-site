from django.shortcuts import render, get_object_or_404
from .models import Review
from games.models import Game
from django.contrib.auth.models import User

# Create your views here.
def review_list(request):
    reviews = Review.objects.all()
    review_data = []  

    for review in reviews:
        review_with_user_title = {
            'review': review,
            'user': review.user,
            'title': review.game.title,
        }
        review_data.append(review_with_user_title)

    return render(request, 'reviews/review_list.html', {'review_data': review_data})

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    reviews = game.reviews.all()

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

    return render(request, 'game_detail.html', {'game': game, 'reviews': reviews, 'form': form})

def submit_review(request):
    if request.method == 'POST':
        return render(request, 'reviews/review_list.html')
    return render(request, 'reviews/submit_review.html')

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'reviews/review_detail.html', {'review': review})

