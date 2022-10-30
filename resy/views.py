from distutils.file_util import move_file
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Reservation, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    searchTerm = request.GET.get('searchReservation')
    if searchTerm:
        reservations = Reservation.objects.filter(title__icontains=searchTerm)
    else:
        reservations = Reservation.objects.all()
    return render(request, 'home.html', 
    {'searchTerm' : searchTerm, 'reservations' : reservations})

def about(request):
    return render(request, 'about.html')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})

@login_required
def createreview(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)

    if request.method == 'GET':
        return render(request, 'createreview.html', {'form' :ReviewForm(), 'reservation': reservation})

    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.reservation = reservation
            newReview.save()
            return redirect('detail', newReview.reservation.id)
        except ValueError:
            return render(request, 'createreview.html', {'form': ReviewForm(), 'error':'bad data passed in'})
@login_required
def updatereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)

    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'updateview.html', {'review': review, 'form': form})

    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('detail', review.reservation.id)
        
        except ValueError:
            return render(request, 'updatereview.html',
            {'review': review, 'form': form,
            'error': 'Bad data in form'})

def deletereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id,
    user=request.user)
    review.delete()
    return redirect('detail', review.reservation.id)