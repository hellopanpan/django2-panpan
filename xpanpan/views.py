# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import AddForm
from .models import Person

def index(request):
  print()
  return HttpResponse(list(Person.objects.values()))
# Create your views here.
def main(request): 
  return render(request, 'home.html')

def add(request): 
  Person.objects.create(name = 'panpan', age = 200)
  form = AddForm(request.GET)
  if form.is_valid():
    num = int(request.GET['a']) + int(request.GET['b']) + 100
    dict1 = {'a': num}
    return JsonResponse(dict1)
  else: 
    form = AddForm
    return JsonResponse(form)