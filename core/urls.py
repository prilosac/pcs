from django.urls import path
from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^store/$', views.store, name='store'),
    url(r'^store/(?P<pk>\d+)/$', views.ControllerView.as_view()),
    url(r'^mods/$', views.mods, name='mods'),
    url(r'^mods/(?P<slug>[\w.\-]+)/$', views.ModView.as_view()),
]
