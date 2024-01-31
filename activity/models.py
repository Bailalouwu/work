from django.db import models

class User(models.Model): #Usuarios
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

class Category (models.Model): #Categoria gym, calistenia, cardio...
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Exercises (models.Model): #Tabla de ejercicios
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Rutine (models.Model): #Pecho, espalda, brazo...
    name = models.CharField(max_length=30)
    exercises = models.ManyToManyField(Exercises)
    repetitions = models.IntegerField(default=0)
    series = models.IntegerField(default=0)
    description = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class Register (models.Model): #Registros de actividad
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)