from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Degree(models.Model):
	idDegree = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=25)
	faculty	 = models.CharField(max_length=25)
	numberOfCredits = models.IntegerField()
	numberOfAcademicYears = models.IntegerField()
	
	def __unicode__(self):
		return self.name


class Teacher(models.Model):
	idTeacher = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=25)
	sexe = models.CharField(max_length=1)
	nationality = models.CharField(max_length=25)
	
	def __unicode__(self):
		return self.name


class Subject(models.Model):
	idSubject = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=25)
	numberOfCredits = models.IntegerField()
	teacher = models.ForeignKey(Teacher)	
	degree = models.ForeignKey(Degree)

	def __unicode__(self):
		return self.name


class Evaluation(models.Model):
	subject = models.ForeignKey(Subject)
	teacher = models.ForeignKey(Teacher)
	RATING_CHOICES = ((1, 'Un'), (2, 'Dos'), (3, 'Tres'), (4, 'Quatre'), (5, 'Cinc'), (6, 'Sis'), (7, 'Set'), (8, 'Vuit'), (9, 'Nou'), (10, 'Deu'))	
	numericEvaluation = models.PositiveSmallIntegerField('Rating (stars)',blank=False,default=5,choices=RATING_CHOICES)
	comment=models.CharField(max_length=25,blank=True,null=True)
	user=models.ForeignKey(User,null=True)
	date=models.DateField(default=date.today)
	def __unicode__(self):
		return self.teacher.name+self.subject.name+str(self.numericEvaluation)

class Review(models.Model):
	RATING_CHOICES = ((1,'Un'),(2,'Dos'),(3,'Tres'),(4,'Quatre'),(5,'Cinc'))
	rating = models.PositiveSmallIntegerField('Ratings (stars)', blank=False, default=3, choices=RATING_CHOICES)
	comment = models.TextField(blank=True, null=True)
	teacher = models.ForeignKey(Teacher)
	user = models.ForeignKey(User, blank=False)
	date = models.DateField(default=date.today)
	
