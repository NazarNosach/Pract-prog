from django.shortcuts import render
from .models import Movie
def KinoZal_home(request):
    news = Movie.objects.order_by('-date')
    return render(request,'KinoZal/KinoZal_home.html', {'KinoZal': KinoZal})
