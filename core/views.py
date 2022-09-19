from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def profile(request):
    return render(request, 'core/profile.html')

def gallery(request):
    return render(request, 'core/gallery.html')

def store(request):
    return render(request, 'core/store.html')

def mods(request):
    return render(request, 'core/mods.html')

