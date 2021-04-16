from django.urls import path
#from . import views
from .views import adopet_app

urlpatterns = [
 path('', adopet_app.index, name="index"),
 path('dogs/', adopet_app.adop_dogs, name="adop_dogs"),
 path('cats/', adopet_app.adop_cats, name="adop_cats"),
 path('others/', adopet_app.adop_others, name="adop_others"),
 path('adoptionInfo/', adopet_app.adoption_info, name="adoption_info"),
 path('dogtraining/', adopet_app.dog_training, name="dog_training"),
 path('cattraining/', adopet_app.cat_training, name="cat_training"),
 path('basiccare/', adopet_app.basic_care, name="basic_care"),
 path('aboutus/', adopet_app.about_us, name="about_us"),
 path('directory/', adopet_app.directory, name="directory"),
]