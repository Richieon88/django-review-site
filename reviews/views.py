from django.shortcuts import render, get_object_or_404
from .models import Review


# Create your views here.
def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

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