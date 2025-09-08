from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.events, name='events'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('resources/', views.resources, name='resources'),
]