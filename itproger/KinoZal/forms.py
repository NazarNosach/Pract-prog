from .models import Booking
from django.forms import ModelForm, TextInput, DateTimeInput, NumberInput


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['movie', 'user_id', 'seats', 'booking_date']

        widgets = {
            "movie": TextInput(attrs={'class': 'form-control', 'placeholder': 'Movie name'}),
            "user_id": TextInput(attrs={'class': 'form-control', 'placeholder': 'User id'}),
            "seats": NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of seats'}),
            "booking_date": DateTimeInput(attrs={'class': 'form-control'}),
        }
