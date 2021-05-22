from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from django.views.generic import CreateView

from ..forms import AdoptantSignUpForm
from ..models import User

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
        return redirect('index')