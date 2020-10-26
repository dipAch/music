import datetime

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
    rating = models.IntegerField(default=0, choices=Score.choices, db_index=True)
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
    rating = models.IntegerField(default=0, choices=Score.choices, db_index=True)
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
