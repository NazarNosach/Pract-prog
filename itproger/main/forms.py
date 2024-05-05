from .models import Booking, Movie
from django.forms import ModelForm, TextInput, DateTimeInput, NumberInput


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['movie', 'user_id', 'seats', 'booking_date']

        widgets = {
            "movie": TextInput(attrs={'class': 'form-control', 'placeholder': 'Movie name'}),
            "user_id": NumberInput(attrs={'class': 'form-control', 'placeholder': 'User id'}),
            "seats": NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of seats'}),
            "booking_date": DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Session date'})
        }

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'release_date', 'director', 'session_time']

        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Movie name'}),
            "director": TextInput(attrs={'class': 'form-control', 'placeholder': 'User id'}),
            "session_time": NumberInput(attrs={'class': 'form-control', 'placeholder': 'Session time'}),
            "release_date": DateTimeInput(attrs={'class': 'form-control'}),
        }