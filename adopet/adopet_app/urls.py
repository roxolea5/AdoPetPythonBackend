from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name="index"),
 path('dogs/', views.adop_dogs, name="adop_dogs"),
 path('cats/', views.adop_cats, name="adop_cats"),
 path('others/', views.adop_others, name="adop_others"),
 path('adoptionInfo/', views.adoption_info, name="adoption_info"),
 path('dogtraining/', views.dog_training, name="dog_training"),
 path('cattraining/', views.cat_training, name="cat_training"),
 path('basiccare/', views.basic_care, name="basic_care"),
 path('aboutus/', views.about_us, name="about_us"),
 path('directory/', views.directory, name="directory"),
]