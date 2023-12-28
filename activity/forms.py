from django import forms
from .models import *

class catgo_Form(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class exer_Form(forms.ModelForm):
    class Meta:
        model = Exercises
        fields = '__all__'

class ruti_Form(forms.ModelForm):
    class Meta:
        model = Rutine
        fields = ('name','description')
