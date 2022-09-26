from django.shortcuts import render
from core.models import *

def index(request):
    images = GalleryImage.objects.all()
    return render(request, 'core/index.html', context={'carousel_start': images[0], 'carousel_images': images[1:]})

def profile(request):
    return render(request, 'core/profile.html')

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'core/gallery.html', context={'images': images})

def store(request):
    controllers = Controller.objects.filter(hidden=False)
    return render(request, 'core/store.html', context={'controllers': controllers})

def mods(request):
    return render(request, 'core/mods.html')

