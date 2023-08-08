from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Finch

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(req):
    return render(req, 'about.html')


def index(req):
    finches = get_list_or_404(Finch)
    return render(req, 'finches/index.html', {
        'finches': finches,
    })


def detail(req, id):
    finch = get_object_or_404(Finch, id=id)
    return render(req, 'finches/detail.html', {"finch": finch})
