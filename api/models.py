from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

# if we delete the movie we will cascade and delete the rating as well.
class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)

