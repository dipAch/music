from django.contrib.auth.models import User
from rest_framework import serializers

from mutecloud.models import (Song, Genre, Playlist, Album,
                              Recommendation, Artist)


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'is_staff']


class ArtistSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Artist
        fields = ['url', 'albums', 'songs', 'genres', 'name']


class GenreSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Genre
        fields = ['url', 'name', 'songs', 'albums', 'artists']


class AlbumSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Album
        fields = ['url', 'name', 'genres', 'rating', 'reviewers',
                  'released_on', 'album_length']


class SongSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Song
        fields = ['url', 'name', 'album', 'genres', 'released_on',
                  'song_length', 'rating', 'reviewers']


class PlaylistSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Playlist
        fields = ['url', 'user', 'songs', 'name', 'created_on']


class RecommendationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Recommendation
        fields = ['url', 'from_user', 'song', 'recommended_on', 'album',
                  'genre', 'artist']
