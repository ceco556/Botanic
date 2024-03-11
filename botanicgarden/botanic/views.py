from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Plant
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class UserPlantPortfolio(ListView, LoginRequiredMixin):
  model = Plant
  context_object_name = 'plants'
  template_name = 'user_portfolio.html'

  def get_queryset(self):
    return self.request.user.plants.all()
# Create your views here.
def index(request):
  plant_list = Plant.objects.all()
  template = loader.get_template("index.html")
  context = {
    "plant_list": plant_list,
  }
  return HttpResponse(template.render(context, request))


def show_plant(request, plant_id):
  plant = Plant.objects.get(pk=plant_id)
  
  template = loader.get_template("plant.html")
  context = {
    "plant": plant,
  }
  return HttpResponse(template.render(context, request))


def login_user(request):
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    print(username)
    print(password)
    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)

      return redirect('index')
    else:
      print("Something went wrong.")
  else:
    return render(request, 'login.html', {})


def logout_user(request):
  logout(request)
  return redirect('index')


def register_user(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      user = authenticate(username=username, password=password)
      login(request, user)
      return redirect('index')
  else:
    form = UserCreationForm()

  return render(request, 'register.html', {'form':form,})