from django.urls import path
from .views import *

app_name = 'activity'

urlpatterns = [
    path('', main_activity),
    path('ejercicios/', exercises_create),
    path('categorias/',category_create),
    path('rutinas/',rutine_create)
]
