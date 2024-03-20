from django.shortcuts import render, get_object_or_404
from .models import Review


# Create your views here.
def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'reviews/review_detail.html', {'review': review})

def submit_review(request):
    if request.method == 'POST':
        return render(request, 'reviews/review_list.html')
    return render(request, 'reviews/submit_review.html')