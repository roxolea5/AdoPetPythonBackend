from django.shortcuts import render

from django.http import HttpResponse

from .models import Pet

# Create your views here.
def index(request):
    return render(request, "index.html")

def adop_dogs(request):
    dogs=Pet.objects.filter(category="Perro")

    return render(request, "dogs.html", {"dogs":dogs})

def adop_cats(request):
    cats=Pet.objects.filter(category="Gato")

    return render(request, "cats.html", {"cats":cats})

def adop_others(request):
    others=Pet.objects.filter(category="Otro")

    return render(request, "others.html")

def adoption_info(request):
    return render(request, "adoptionInfo.html")

def dog_training(request):
    return render(request, "dogtraining.html")

def cat_training(request):
    return render(request, "cattraining.html")
    
def basic_care(request):
    return render(request, "basiccare.html")

def about_us(request):
    return render(request, "aboutus.html")

def directory(request):
    return render(request, "directory.html")