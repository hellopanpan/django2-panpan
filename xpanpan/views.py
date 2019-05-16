# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import AddForm
from .models import Person
from .models import Movies
import json


def index(request):
  data = Movies.objects.all().to_json()
  # json.loads() 处理为字典
  res = {
    "code": 0,
    "msg": "success",
    "data": json.loads(data)
  }
  return JsonResponse(res)
def index2(request):
  data = Person.objects.all().skip(2).to_json()
  # json.loads() 处理为字典
  res = {
    "code": 0,
    "msg": "success",
    "data": json.loads(data)
  }
  return JsonResponse(res)
# Create your views here.
def main(request): 
  data = Movies.objects.all().order_by('price').to_json()
  context = {
    "data": json.loads(data)
  }
  return render(request, 'home.html', context)

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