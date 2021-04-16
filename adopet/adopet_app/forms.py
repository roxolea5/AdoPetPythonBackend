from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email', )
    
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)

class RescuerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', )
        
        def save(self, commit=True):
            user = super().save(commit=False)
            user.is_rescuer = True
            if commit:
                user.save()
            return user

class AdoptantSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', )
        
        def save(self, commit=True):
            user = super().save(commit=False)
            user.is_adoptant = True
            if commit:
                user.save()
            return user
