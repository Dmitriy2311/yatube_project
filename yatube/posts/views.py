from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(reguest):
    return HttpResponse('Главная страница')


def group_post(reguest, slug):
    return HttpResponse('Список групп {slug}')