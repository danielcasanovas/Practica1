from django.db import models

# Create your models here.

#class Sobre(models.Model):
#	date = models.DateTimeField()
#	amount = models.IntegerField()
#	concept = models.TextField(max_length=100)

class Teacher(models.Model):
	edat = models.IntegerField()
	name = models.CharField(max_length=100)
	
