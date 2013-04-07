from django.db import models

# Create your models here.

class Degree(models.Model):
	idDegree = models.TextField(primary_key=True, max_length=10)
	name = models.CharField(max_length=25)
	faculty	 = models.CharField(max_length=25)
	numberOfCredits = models.IntegerField()
	numberOfAcademicYears = models.IntegerField()
	
	def __unicode__(self):
		return self.name


class Teacher(models.Model):
	idTeacher = models.TextField(primary_key=True, max_length=10)
	name = models.CharField(max_length=25)
	sexe = models.CharField(max_length=1)
	nationality = models.CharField(max_length=25)
	
	def __unicode__(self):
		return self.name+" - "+self.idTeacher


class Subject(models.Model):
	idSubject = models.TextField(primary_key=True, max_length=10)
	name = models.CharField(max_length=25)
	numberOfCredits = models.IntegerField()
	teacher = models.ForeignKey(Teacher)	
	degree = models.ForeignKey(Degree)

	def __unicode__(self):
		return self.name


class Evaluation(models.Model):
	subject = models.ForeignKey(Subject)
	teacher = models.ForeignKey(Teacher)
	numericEvaluation = models.IntegerField()
	
	def __unicode__(self):
		return self.numericEvaluation




	
