from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
from rest_framework.generics import ListCreateAPIView


class CustomSongPagination(PageNumberPagination):
    page_size = 1


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomSongPagination
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        return serializer.save(album=Album.objects.get(pk=self.kwargs.get("pk")))
