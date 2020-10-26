from django.contrib.auth.models import User #, Group
from django.db import transaction
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from mutecloud.models import (Song, Playlist, Album, Genre,
                              Recommendation, Artist)
from mutecloud.serializers import (UserSerializer, # GroupSerializer,
                                   SongSerializer, PlaylistSerializer,
                                   GenreSerializer, AlbumSerializer,
                                   RecommendationSerializer, ArtistSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('-id')
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    @action(detail=True, url_path='rate-song', methods=['get', 'put'])
    @transaction.atomic
    def rate_song(self, request, pk=None, **kwargs):
        song = self.queryset.get(id=pk)

        if request.method == 'PUT':
            numerator = (song.rating * song.reviewers) + request.data['rating']
            denominator = song.reviewers + 1
            new_rating = numerator // denominator
            song.rating = new_rating
            song.reviewers += 1
            song.save()

        song_serializer = self.serializer_class(
            song,
            context={'request': request})

        return Response(
            status=status.HTTP_202_ACCEPTED,
            data=song_serializer.data)

    @action(detail=True, url_path='recommend-song', methods=['put'])
    @transaction.atomic
    def recommend_song(self, request, pk=None, **kwargs):
        song = self.queryset.get(id=pk)
        resp_status = status.HTTP_200_OK

        if request.method == 'PUT':
            for_user = User.objects.get(id=request.data['user'])
            new_recommendation = Recommendation.objects.create(
                from_user=request.user,
                for_user=for_user,
                song=song)
            resp_status = status.HTTP_202_ACCEPTED

        song_serializer = self.serializer_class(
            song,
            context={'request': request})

        return Response(
            status=resp_status,
            data=song_serializer.data)


class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all().order_by('-id')
    serializer_class = RecommendationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        recommendations = self.queryset.filter(
            for_user=request.user).all()
        recommendations_serializer = self.serializer_class(
            recommendations,
            context={'request': request},
            many=True)

        return Response(
            status=status.HTTP_200_OK,
            data=recommendations_serializer.data)


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('-released_on')
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    @action(detail=True, url_path='recommend-album', methods=['put'])
    @transaction.atomic
    def recommend_album(self, request, pk=None, **kwargs):
        album = self.queryset.get(id=pk)
        resp_status = status.HTTP_200_OK

        if request.method == 'PUT':
            for_user = User.objects.get(id=request.data['user'])
            new_recommendation = Recommendation.objects.create(
                from_user=request.user,
                for_user=for_user,
                album=album)
            resp_status = status.HTTP_202_ACCEPTED

        album_serializer = self.serializer_class(
            album,
            context={'request': request})

        return Response(
            status=resp_status,
            data=album_serializer.data)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by('id')
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    @action(detail=True, url_path='recommend-genre', methods=['put'])
    @transaction.atomic
    def recommend_genre(self, request, pk=None, **kwargs):
        genre = self.queryset.get(id=pk)
        resp_status = status.HTTP_200_OK

        if request.method == 'PUT':
            for_user = User.objects.get(id=request.data['user'])
            new_recommendation = Recommendation.objects.create(
                from_user=request.user,
                for_user=for_user,
                genre=genre)
            resp_status = status.HTTP_202_ACCEPTED

        genre_serializer = self.serializer_class(
            genre,
            context={'request': request})

        return Response(
            status=resp_status,
            data=genre_serializer.data)


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('name')
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    @action(detail=True, url_path='recommend-artist', methods=['put'])
    @transaction.atomic
    def recommend_artist(self, request, pk=None, **kwargs):
        artist = self.queryset.get(id=pk)
        resp_status = status.HTTP_200_OK

        if request.method == 'PUT':
            for_user = User.objects.get(id=request.data['user'])
            new_recommendation = Recommendation.objects.create(
                from_user=request.user,
                for_user=for_user,
                artist=artist)
            resp_status = status.HTTP_202_ACCEPTED

        artist_serializer = self.serializer_class(
            artist,
            context={'request': request})

        return Response(
            status=resp_status,
            data=artist_serializer.data)


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all().order_by('-created_on')
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        playlists = self.queryset.filter(user=self.request.user).all()
        playlists_serializer = self.serializer_class(
            playlists,
            context={'request': request},
            many=True)

        return Response(
            status=status.HTTP_200_OK,
            data=playlists_serializer.data)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        playlist_songs = Song.objects.filter(
            id__in=request.data['songs']).all()
        new_playlist = Playlist.objects.create(
            name=request.data['name'],
            user=request.user)
        new_playlist.songs.set(playlist_songs)
        new_playlist.save()
        playlist_serializer = self.serializer_class(
            new_playlist,
            context={'request': request})

        return Response(
            status=status.HTTP_201_CREATED,
            data=playlist_serializer.data)

    @action(detail=True, url_path='remove-song', methods=['get', 'put'])
    @transaction.atomic
    def remove_song_from_playlist(self, request, pk=None, **kwargs):
        playlist = self.queryset.get(id=pk)
        resp_status = status.HTTP_200_OK

        if request.method == 'PUT':
            songs = Song.objects.filter(
                id__in=request.data['songs']).all()

            for song in songs:
                playlist.songs.remove(song)

            playlist.save()

            resp_status = status.HTTP_202_ACCEPTED

        playlist_serializer = self.serializer_class(
            playlist,
            context={'request': request})

        return Response(
            status=resp_status,
            data=playlist_serializer.data)

    @action(detail=True, url_path='add-song', methods=['get', 'put'])
    @transaction.atomic
    def add_song_to_playlist(self, request, pk=None, **kwargs):
        playlist = self.queryset.get(id=pk)
        resp_status = status.HTTP_200_OK

        if request.method == 'PUT':
            songs = Song.objects.filter(
                id__in=request.data['songs']).all()

            playlist.songs.set(playlist.songs.all() | songs)

            playlist.save()

            resp_status = status.HTTP_202_ACCEPTED

        playlist_serializer = self.serializer_class(
            playlist,
            context={'request': request})

        return Response(
            status=resp_status,
            data=playlist_serializer.data)
