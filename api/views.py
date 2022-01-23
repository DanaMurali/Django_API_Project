from rest_framework import viewsets
from api.serializers import MovieSerializer, RatingSerializer
from api.models import Movie, Rating

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
