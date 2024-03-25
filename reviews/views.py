from django.shortcuts import render, get_object_or_404, redirect
from .models import Review, Comment
from .forms import ReviewForm
from games.models import Game
from games.views import game_detail

# Create your views here.
def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    comments = review.comments.all()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.review = review
            new_comment.user = request.user
            new_comment.save()
            return redirect('review_detail', pk=pk)
    else:
        comment_form = CommentForm()
    
    return render(request, 'reviews/review_detail.html', {'review': review, 'comments': comments, 'comment_form': comment_form})

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
