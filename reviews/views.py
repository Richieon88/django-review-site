from django.shortcuts import render, get_object_or_404, redirect
from .models import Review, Comment, Like
from .forms import ReviewForm, CommentForm
from games.models import Game
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse


# Create your views here.
def review_list(request):
    reviews = Review.objects.all()
    review_data = []
    for review in reviews:
        review_data.append({
            'review': review,
            'user': review.user,
            'title': review.game.title
        })
    return render(
        request,
        'reviews/review_list.html',
        {'review_data': review_data}
    )


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
            return redirect('reviews:review_detail', pk=pk)
    else:
        comment_form = CommentForm()
    return render(request, 'reviews/review_detail.html', {
        'review': review,
        'comments': comments,
        'comment_form': comment_form
    })


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
            return redirect('games:game_detail', pk=game_id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/submit_review.html', {'form': form})


def profile(request):
    user = request.user
    reviews = user.review_set.all()
    return render(request, 'reviews/profile.html', {'reviews': reviews})


def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Review deleted successfully.')
        return redirect('reviews:profile')
    else:
        messages.error(request, 'Failed to delete review.')
        return redirect('reviews:profile')


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user == comment.user:
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
    else:
        messages.error(request, 'You are not allowed to delete this comment.')

    return redirect('reviews:review_detail', pk=comment.review.pk)


def like_comment(request):
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        if comment_id:
            comment = get_object_or_404(Comment, pk=comment_id)
            user = request.user

            if Like.objects.filter(comment=comment, user=user).exists():
                Like.objects.filter(comment=comment, user=user).delete()
                comment.likes_count -= 1
                comment.save()
                liked = False
            else:
                Like.objects.create(comment=comment, user=user)
                comment.likes_count += 1
                comment.save()
                liked = True

            data = {
                'liked': liked,
                'likes_count': comment.likes_count,
            }
            return JsonResponse(data)
        else:
            return JsonResponse(
                {'error': 'comment_id not provided'},
                status=400
            )
    else:
        return JsonResponse(
            {'error': 'Invalid request method'},
            status=405
        )
