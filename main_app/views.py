from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Finch
from .forms import create_bootstrap_form

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


class CreateFinch(CreateView):
    form_class = create_bootstrap_form(model=Finch, fields='__all__')
    template_name = 'finches/create.html'


class UpdateFinch(UpdateView):
    form_class = create_bootstrap_form(
        model=Finch, fields=['breed', 'description', 'age'])
    model = Finch
    template_name = 'finches/create.html'


class DeleteFinch(DeleteView):
    model = Finch
    template_name = 'finches/confirm_delete.html'
    success_url = '/finches'
