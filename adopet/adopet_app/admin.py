from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm, AdoptantSignUpForm, RescuerSignUpForm
from .models import User, Pet, Questionary, Request

# Personalizing models on admin
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('id', 'email', 'name_of_user', 'first_name', 'last_name', 'date_of_birth', 'is_adoptant', 'is_rescuer', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_rescuer', 'is_adoptant','is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_adoptant', 'is_rescuer','is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','name_of_user', 'first_name', 'last_name', 'date_of_birth', 'is_adoptant', 'is_rescuer', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

class PetAdmin(admin.ModelAdmin):
    # Override __str__ method
    list_display = ("id", "name", "category", "sex", "size", "status", "user_rescuer_id")

class QuestionaryAdmin(admin.ModelAdmin):
    # Override __str__ method
    list_display = ("id", "address_street", "address_ext_num", "address_city", "address_zip_code", "pet_owner", "family_members", "family_agreement", "user_applicant_id", "status")

class RequestAdmin(admin.ModelAdmin):
    # Override __str__ method
    list_display = ("id", "pet_id", "applicant_user_id", "approver_user_id", "status")


# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.register(Pet, PetAdmin)
admin.site.register(Questionary, QuestionaryAdmin)
admin.site.register(Request, RequestAdmin)
