from django.urls import path

from . import views

urlpatterns = [
    #Главная страница
    path('', views.index),
    #Список групп
    path('group/<slug:slug>/', views.group_post)
] 