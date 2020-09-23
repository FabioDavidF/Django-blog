from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Lughzin',
        'title': 'Why I use pineaple juice in my TP',
        'content': 'This is a serious topic',
        'date_posted': 'September 23rd 2020'
    },
    {
        'author': 'Not me',
        'title': 'Why I DONT use pineaple juice in my TP',
        'content': 'This is not a serious topic',
        'date_posted': 'September 24th 2020'
    }
]

# Create your views here.

def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {
        'title': 'About'
    })