from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/profile/', views.profile, name='profile'),
    path('gallery/', views.gallery, name='gallery'),
    path('store/', views.store, name='store'),
    path('mods/', views.mods, name='mods'),
]
