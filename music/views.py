from django.http import HttpResponse

def index(request):
	return HttpResponse('<h1> Hello ! This is the music homepage!</h1>')