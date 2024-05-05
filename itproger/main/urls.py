from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create_booking', views.create_booking, name='create_booking'),
    path('about', views.about, name='about'),
    path('booking',views.booking_page, name='booking')
]
