from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie, Booking
from .forms import BookingForm


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'main/index.html', {'movies': movies})



def about(request):
    return render(request, 'main/about.html')

def booking_page(request):
    news = Booking.objects.all()
    return render(request,'main/bookings.html', {'news': news})

def create_booking(request):
    error=''
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            # Extract field names with errors
            invalid_fields = [field for field, errors in form.errors.items()]

            # Construct error message
            error = f"The following fields are incorrect: {', '.join(invalid_fields)}"

    form = BookingForm()

    data ={
        'form':form,
        'error': error
    }

    return render(request, 'main/create_booking.html',data)