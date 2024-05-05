from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    release_date = models.DateField()
    session_time = models.IntegerField()

    def __str__(self):
        return self.title

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    seats = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.movie.title} by User {self.user_id}"
