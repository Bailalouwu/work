from django.shortcuts import redirect, render
from .forms import *
from .models import *

# INSTRUCCIONES PARA EL TEMPLATE PRINCIPAL
def main_activity (request):
    exercises = Exercises.objects.all()
    return render(request,'main.html', {'exercises':exercises})



# INSTRUCCIONES PARA EL TEMPLATE EJERCICIOS
def exercises_create (request):
    list = Category.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        category_id = request.POST['category']
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            category = None
        Exercises.objects.create(name=name,description=description,category=category)
    return render(request, 'exercises.html',{'list': list})


# INSTRUCCIONES PARA EL TEMPLATE CATEGORIA
def category_create(request):
    formset = catgo_Form()
    if request.method == 'POST':
        formset = catgo_Form(request.POST)
        if formset.is_valid():
            formset.save()
        else:
            print(formset.errors)
    context = {
        'formset' : formset
    }
    return render(request, 'category.html',context)


# INSTRUCCIONES PARA EL TEMPLATE RUTINAS
def rutine_create (request):
    if request.method == 'POST':
        form = ruti_Form(request.POST)
        if form.is_valid():
            rutine = form.save(commit=False)
            rutine.save()

            exercises_list = request.POST.getlist('exercises')
            for exercise_id in exercises_list:
                exercise = Exercises.objects.get(pk=exercise_id)
                rutine.exercises.add(exercise)
    else:
        form = ruti_Form()
    exercises = Exercises.objects.all()
    return render(request,'rutine.html', {'form': form, 'exercises': exercises})