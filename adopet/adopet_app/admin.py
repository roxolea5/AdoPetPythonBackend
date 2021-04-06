from django.contrib import admin
from .models import Role, User, Pet, Questionary, Request

# Personalizing models on admin
class RoleAdmin(admin.ModelAdmin):
    # Override __str__ method
    list_display = ("id", "role", "description", "status")

class UserAdmin(admin.ModelAdmin):
    # Override __str__ method
    list_display = ("id", "username", "first_name", "last_name", "status", "role_id")

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

# Register your models here.
admin.site.register(Role, RoleAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Pet, PetAdmin)
admin.site.register(Questionary, QuestionaryAdmin)
admin.site.register(Request, RequestAdmin)
