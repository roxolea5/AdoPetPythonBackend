from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models import Pet, User
#imports for SignUp
from django.views.generic import TemplateView, CreateView
from ..forms import AdoptantSignUpForm, RescuerSignUpForm
# Create your views here.



from django.shortcuts import redirect, render
from django.views.generic import TemplateView


def signup(request):
    context = {}
    
    return render(request, 'registration/signup.html', context)

class AdoptantSignUpView(CreateView):
    model = User
    form_class = AdoptantSignUpForm
    template_name = 'registration/signup_form.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'adoptant'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return render('index.html')

class RescuerSignUpView(CreateView):
    model = User
    form_class = RescuerSignUpForm
    template_name = 'registration/signup_form.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'rescuer'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return render('index.html')

def home(request):
    return render(request, 'index.html')

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
    return render(request, "others.html", {"others":others})

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
