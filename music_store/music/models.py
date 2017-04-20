from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length = 250)
    album_title = models.CharField(max_length = 250)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)  #froeign key is used when this is part of something else.
    # on delete -when we delete any album it also delete all song link to it.
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default = False)

    def __str__(self):
        return self.song_title







# when you change anything in models then run command
#1-makemigrations and then migrate
# when you do 1st time 2nd command use sqlmigrate 0001-nameoffile
