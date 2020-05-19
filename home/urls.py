from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    
    path("", views.index,name='home'),
    path('about', views.about,name='about'),
    path('login', views.login,name='login'),
    path('register', views.register,name='register'),
    path('search', views.search,name='search1'),
    path('blood', views.blood,name='blood'),
    path('store', views.store,name='store'),





]