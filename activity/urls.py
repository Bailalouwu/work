from django.urls import path
from .views import *

app_name = 'activity'

urlpatterns = [
    path('', main_activity),
    path('ejercicios/', exercises_create),
    path('categorias/',category_create),
    path('rutinas/',rutine_create),
    path('delete_exercise/<int:id>/', delete_exercise, name="delete_exercise"),
    path('update_exercise/<int:id>/', update_exercise, name="update_exercise"),
    path('change_exercise/<int:id>/', change_exercise, name="change_exercise"),
]
