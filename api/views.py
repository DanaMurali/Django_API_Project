from rest_framework import viewsets, status
from rest_framework.response import Response
from api.serializers import MovieSerializer, RatingSerializer
from api.models import Movie, Rating
from rest_framework.decorators import action

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    # making own custom model
    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        response = {'message': 'it is working'}
        return Response(response, status=status.HTTP_200_OK)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
