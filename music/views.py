from django.http import HttpResponse
from music.models import Album
from django.shortcuts import render

def index(request):
	all_albums = Album.objects.all()
	context = {'all_albums' : all_albums}
	return render(request, 'music/index.html', context)

def details(request,album_id):
	return HttpResponse('<h1> The album id is: ' + str(album_id) + '</h1>')