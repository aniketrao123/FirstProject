from django.http import Http404
from music.models import Album
from django.shortcuts import render,get_object_or_404

def index(request):
	all_albums = Album.objects.all()
	context = {'all_albums':all_albums}
	return render(request, 'music/index.html', context)

def details(request,album_id):
	album = get_object_or_404(Album,id=album_id)
	context = {'album':album}
	return render(request, 'music/detail.html', context)
