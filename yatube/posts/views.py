from django.http import HttpResponse #from django.shortcuts import render


def index(request):
    return HttpResponse('Главная страница')


def group_post(request, slug):
    return HttpResponse(f'Группа номер {slug}')
