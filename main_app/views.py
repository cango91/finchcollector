import uuid
import boto3
import os
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.urls import reverse, reverse_lazy
from .models import Finch, Feeding, Toy, Photo
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

    feeding_form = create_bootstrap_form(
        model=Feeding, fields=['date', 'meal'])

    available_toys = Toy.objects.all().exclude(
        id__in=finch.toys.all().values_list('id'))

    return render(req, 'finches/detail.html', {
        "finch": finch,
        "feeding_form": feeding_form,
        "available_toys": available_toys
    })


class CreateFinch(CreateView):
    form_class = create_bootstrap_form(
        model=Finch, fields=['name', 'breed', 'description', 'age'])
    template_name = 'finches/create.html'


class UpdateFinch(UpdateView):
    form_class = create_bootstrap_form(
        model=Finch, fields=['breed', 'description', 'age'])
    model = Finch
    template_name = 'finches/create.html'


class DeleteFinch(DeleteView):
    model = Finch
    template_name = 'finches/confirm_delete.html'
    success_url = reverse_lazy('finches:index')


def add_feeding(req, pk):
    feeding_form = create_bootstrap_form(
        model=Feeding, fields=['date', 'meal'])(req.POST)
    if (feeding_form.is_valid()):
        feeding = feeding_form.save(commit=False)
        feeding.finch_id = pk
        feeding.save()
    return redirect('finches:detail', id=pk)


class ListToys(ListView):
    model = Toy
    template_name = 'toys/index.html'


class DetailToy(DetailView):
    model = Toy
    template_name = 'toys/detail.html'


class CreateToy(CreateView):
    form_class = create_bootstrap_form(model=Toy, fields='__all__')
    template_name = 'toys/create.html'


class UpdateToy(UpdateView):
    form_class = create_bootstrap_form(model=Toy, fields=['name', 'color'])
    model = Toy
    template_name = 'toys/create.html'


class DeleteToy(DeleteView):
    template_name = 'toys/confirm_delete.html'
    model = Toy
    success_url = reverse_lazy('finches:toys')


def associate_toy(req, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    url = reverse('finches:detail',args=[finch_id]) + '#toys-section'
    return redirect(url)


def disassociate_toy(req, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.remove(toy_id)
    url = reverse('finches:detail',args=[finch_id]) + '#toys-section'
    return redirect(url)


def add_photo(req, finch_id):
    photo_file = req.FILES.get('photo-file', None)
    if (photo_file):
        s3 = boto3.client('s3')
        # unique key for S3 with image file extension
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, finch_id=finch_id)
        except Exception as e:
            print('An error occured uploading the file to S3')
            print(e)
    return redirect('finches:detail', id=finch_id)
