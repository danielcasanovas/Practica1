from django.db import models

# Create your models here.

class Teacher(models.Model):
	idTeacher = models.TextField(primary_key=True, max_lenght=10)
	name = models.CharField(max_length=25)
	sexe = models.CharField(max_length=1)


class Subject(models.Model):
	idSubject = models.TextField(primary_key=True, max_lenght=10)
	name = models.CharField(max_length=25)
	numberOfCredits = models.IntegerField()
	degree = models.ForeignKey(Degree)

class Degree(models.Model):
	idDegree = models.TextField(primary_key=True, max_lenght=10)
	name = models.CharField(max_length=25)
	name = models.CharField(max_length=25)
	sexe = models.CharField(max_length=1)


	
