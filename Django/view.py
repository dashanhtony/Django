from django.http import HttpResponse
from django.shortcuts import render


# def hello(request):
#     return HttpResponse("Hello world ! ")

def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    context['hello2'] = 'Hello World2!'
    context['athlete_list'] = [
        {'name': 'athlete1', 'sports_played': ['basketball1', 'football1', 'tennis1']},
        {'name': 'athlete2', 'sports_played': ['basketball2', 'football2', 'tennis2']},
        {'name': 'athlete3', 'sports_played': ['basketball3', 'football3', 'tennis3']}
    ]
    context['user'] = 'User'
    context['currentuser'] = 'Currentuser'
    return render(request, 'hello.html', context)

def base(request):
    context = {}
    context['mainbody1'] = 'mainbody1'
    return render(request, 'base.html', context)

def hello2(request):
    context = {}
    context['mainbody2'] = '12321321321'
    return render(request, 'hello2.html', context)