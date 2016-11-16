from __future__ import unicode_literals

from django.db import models

# Create your models here.
# basically a blueprint of your app. This is linked to your database.
# so every variable in a class is a column in your database.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    name = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=150)

    def __str__(self):
    	return self.name + ', ' + self.artist

class Song(models.Model):
 	album_name = models.ForeignKey(Album,on_delete=models.CASCADE)
 	file_type = models.CharField(max_length=100)
 	song_title = models.CharField(max_length=250)
 	def __str__(self):
 		return self.song_title	