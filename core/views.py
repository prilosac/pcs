from django.shortcuts import render
from django.views.generic.detail import DetailView
from core.models import *

def index(request):
    images = GalleryImage.objects.all()
    context = {}
    if images:
        context = {'carousel_start': images[0], 'carousel_images': images[1:]}

    return render(request, 'core/index.html', context=context)

def profile(request):
    return render(request, 'core/profile.html')

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'core/gallery.html', context={'images': images})

def store(request):
    controllers = Controller.objects.filter(hidden=False)
    for controller in controllers:
        price = controller.price - controller.discount
        for mod in controller.mods.all():
            price += mod.price

        controller.total_price = price
        controller.store_image = controller.controllerimage_set.filter(primary=True).first()
    return render(request, 'core/store.html', context={'controllers': controllers})

def mods(request):
    return render(request, 'core/mods.html')

class ModView(DetailView):
    model = Mod
    slug_field = 'slug'
    template_name = 'core/mod.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ControllerView(DetailView):
    model = Controller
    pk_url_kwarg = 'pk'
    template_name = 'core/controller.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['primary_image'] = self.object.controllerimage_set.filter(primary=True).first()
        price = self.object.price - self.object.discount
        for mod in self.object.mods.all():
            price += mod.price

        self.object.total_price = price
        self.object.store_image = self.object.controllerimage_set.filter(primary=True).first()
        return context
    
