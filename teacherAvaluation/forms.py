from django.forms import ModelForm 
from django import forms
from teacherAvaluation.models import *

class AddEvaluation(ModelForm):
	class Meta:
		model = Evaluation

class AddSubject(ModelForm):
	class Meta:
		model = Subject

class AddTeacher(ModelForm):
	class Meta:
		model = Teacher
	
class AddDegree(ModelForm):
	class Meta:
		model = Degree

class UpdateSubject(ModelForm):
	class Meta:
		model = Subject
		exclude = ('idSubject')

class UpdateTeacher(ModelForm):
	class Meta:
		model = Teacher
		exclude = ('idTeacher')

class UpdateEvaluation(ModelForm):
	class Meta:
		model = Evaluation
		exclude = ('id','teacher','subject',)
