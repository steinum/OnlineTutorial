from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1> music app web </h1>')

def detail(request, album_id):
    return HttpResponse('<h2> Details for album id:' + str(album_id) + '</h2>')