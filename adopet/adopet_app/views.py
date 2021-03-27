from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def adop_dogs(request):
    return render(request, "dogs.html")

def adop_cats(request):
    return render(request, "cats.html")

def adop_others(request):
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