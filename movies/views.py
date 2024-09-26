from django.shortcuts import render

def home(request):
    return render(request, 'movies/home.html')

def peliculas(request):
    return render(request, 'movies/peliculas.html')

def about(request):
    return render(request, 'movies/about.html')

def contact(request):
    return render(request, 'movies/contact.html')

def gallery(request):
    return render(request, 'movies/gallery.html')

