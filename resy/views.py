from django.shortcuts import render
from django.http import HttpResponse
from .models import Reservation
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
