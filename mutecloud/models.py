import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import smart_str as smart_unicode

from mutecloud.constants import DATE_FORMAT


class Genre(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return u'Genre Name: %s' % (smart_unicode(self.name))


class Album(models.Model):

    class Score(models.IntegerChoices):
        UNRATED     = 0
        FLOP        = 1
        FADE        = 2
        AVERAGE     = 3
        CLASSIC     = 4
        ALL_TIME    = 5

    genres = models.ManyToManyField(Genre, related_name='albums', db_index=True)
    rating = models.IntegerField(default=0, choices=Score.choices)
    reviewers = models.IntegerField(default=0)
    name = models.TextField(db_index=True)
    released_on = models.DateField(default=datetime.date.today, db_index=True)
    album_length = models.TextField()

    def __unicode__(self):
        return u'Album Name: %s' % (smart_unicode(self.name))


class Song(models.Model):

    class Score(models.IntegerChoices):
        UNRATED     = 0
        FLOP        = 1
        FADE        = 2
        AVERAGE     = 3
        CLASSIC     = 4
        ALL_TIME    = 5

    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, related_name='songs', db_index=True)
    rating = models.IntegerField(default=0, choices=Score.choices)
    reviewers = models.IntegerField(default=0)
    name = models.TextField(db_index=True)
    released_on = models.DateField(default=datetime.date.today, db_index=True)
    song_length = models.TextField()

    def __unicode__(self):
        return u'Song Name: %s' % (smart_unicode(self.name))


class Artist(models.Model):
    albums = models.ManyToManyField(Album, related_name='artists', db_index=True)
    songs = models.ManyToManyField(Song, related_name='artists', db_index=True)
    genres = models.ManyToManyField(Genre, related_name='artists', db_index=True)
    name = models.TextField(db_index=True)

    def __unicode__(self):
        return u'Artist Name: %s' % (smart_unicode(self.name))

class Playlist(models.Model):
    user = models.ForeignKey(User, related_name='playlists', on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song, related_name='playlists', db_index=True)
    name = models.TextField()
    created_on = models.DateField(default=datetime.date.today)

    def __unicode__(self):
        return u'Playlist Name: %s, User: %s' % (
            smart_unicode(self.name), smart_unicode(self.user.username))


class Recommendation(models.Model):
    from_user = models.ForeignKey(
        User, related_name='recommendations_sent', on_delete=models.CASCADE)
    for_user = models.ForeignKey(
        User, related_name='recommendations_recieved', on_delete=models.CASCADE)
    song = models.ForeignKey(
        Song, related_name='recommendations', on_delete=models.CASCADE,
        blank=True, null=True)
    album = models.ForeignKey(
        Album, related_name='recommendations', on_delete=models.CASCADE,
        blank=True, null=True)
    genre = models.ForeignKey(
        Genre, related_name='recommendations', on_delete=models.CASCADE,
        blank=True, null=True)
    artist = models.ForeignKey(
        Artist, related_name='recommendations', on_delete=models.CASCADE,
        blank=True, null=True)
    recommended_on = models.DateField(default=datetime.date.today)

    def __unicode__(self):
        return u'[%s] From User: %s -> User: %s' % (
            self.recommended_on.strftime(DATE_FORMAT),
            smart_unicode(self.from_user.username),
            smart_unicode(self.for_user.username))
