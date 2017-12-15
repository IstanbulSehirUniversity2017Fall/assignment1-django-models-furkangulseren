from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is the movies app homepage</h1>")

def film(request,movie_name):
    return HttpResponse('<h1> This is my site "' +str(movie_name) +'"</h1>' )