from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context , RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, logout,login
from teacherAvaluation.models import *
from django.http import Http404
from django import forms
from teacherAvaluation.forms import *
from django.contrib.auth.forms import UserCreationForm



def mainpage(request):
	variables = Context({
		'titlehead': 'Teacher Avaluation',
		'pagetitle': 'Evaluacio de docencia',
		'contentbody': 'Benvinguts a el aplicatiu de evaluacio de docencia , navega pel menu per veure el llistat de les diferents entitats.'
		})
	context_instance = RequestContext(request)
	return render_to_response('mainpage.html',variables,context_instance)


def registration (request):
	if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
              new_user = form.save()
	      variables = Context({
		'titlehead': 'Teacher Avaluation',
		'pagetitle': 'Evaluacio de docencia',
		'contentbody': 'Registre realitzat correctament.'
		})
              return render_to_response('mainpage.html',variables,context_instance = RequestContext(request))
        else:
            form = UserCreationForm()
        return render(request, "registration/registration.html", {
            'form': form,
        })	


def teacher(request):
	listOfTeachers = Teacher.objects.all()
	variables = Context({
		'titlehead': 'Teacher Avaluation',
		'pagetitle': 'Evaluacio de docencia',
		'contentbody': 'Llistat de Professors:',
		'teachers_list' : listOfTeachers
		})
	context_instance = RequestContext(request)
	return render_to_response('teachers.html',variables,context_instance)

def singular_teacher(request,teacher_id):

	try:
		teacher = Teacher.objects.get(idTeacher=teacher_id)
		variables = Context({
			'contentbody': 'Dades Personals Professor:',
			'titlehead': 'Teacher Avaluation',
			'pagetitle': 'Evaluacio de docencia',
			'nameteacher': teacher.name,
			'sex': teacher.sexe,

			'nationality': teacher.nationality
			})
		context_instance = RequestContext(request)
	except:
		raise Http404
	return render_to_response('single_teacher.html',variables,context_instance)


def degree(request):
	listOfDegrees = Degree.objects.all()
	variables = Context({
		'titlehead': 'Teacher Avaluation',
		'pagetitle': 'Evaluacio de docencia',
		'contentbody': 'Llistat de Carreres:',
		'degrees_list' : listOfDegrees
		})
	context_instance = RequestContext(request)
	return render_to_response('degrees.html',variables,context_instance)

def singular_degree(request,degree_id):
	
	try:
		degree = Degree.objects.get(idDegree=degree_id)
		variables = Context({
			'contentbody': 'Detalls Carrera:',
			'titlehead': 'Teacher Avaluation',
			'pagetitle': 'Evaluacio de docencia',
			'namedegree': degree.name,
			'faculty': degree.faculty,
			'credits': degree.numberOfCredits,
			'years': degree.numberOfAcademicYears
			})
		context_instance = RequestContext(request)
	except:
		raise Http404
	return render_to_response('single_degree.html',variables,context_instance)

def subject(request):
	listOfSubjects = Subject.objects.all()
	variables = Context({
		'titlehead': 'Teacher Avaluation',
		'pagetitle': 'Evaluacio de docencia',
		'contentbody': 'Llistat de Assignatures:',
		'subjects_list' : listOfSubjects
		})
	context_instance = RequestContext(request)
	return render_to_response('subjects.html',variables,context_instance)

def singular_subject(request,subject_id):
	
	try:
		subject = Subject.objects.get(idSubject=subject_id)
		variables = Context({
			'contentbody': 'Detalls assignatura:',
			'titlehead': 'Teacher Avaluation',
			'pagetitle': 'Evaluacio de docencia',
			'namesubject': subject.name,
			'teacher': subject.teacher,
			'credits': subject.numberOfCredits,
			'degree': subject.degree
			})
		context_instance=RequestContext(request)
	except:
		raise Http404
	return render_to_response('single_subject.html',variables,context_instance)

def evaluation(request):
	listOfEvaluation = Evaluation.objects.all()
	variables = Context({
		'titlehead': 'Teacher Avaluation',
		'pagetitle': 'Evaluacio de docencia',
		'contentbody': 'Llistat de Evaluacions - Professors:',
		'evaluation_list' : listOfEvaluation
		})
	context_instance = RequestContext(request)
	return render_to_response('evaluation.html',variables,context_instance)

def evaluation_add (request):
	if request.method == 'POST':
            form = AddEvaluation(request.POST)
            if form.is_valid():
              new_evaluation = form.save()
	      return HttpResponseRedirect('/evaluations/')
        else:
            form = AddEvaluation
        return render(request, "evaluation_add.html", {
            'form': form,'titlehead': 'Teacher Avaluation',
		'pagetitle': 'Evaluacio de docencia',
        },context_instance = RequestContext(request))	

def degree_add (request):
	if request.method == 'POST':
            form = AddDegree(request.POST)
            if form.is_valid():
              new_degree = form.save()
	      return HttpResponseRedirect('/degrees/')
        else:
            form = AddDegree
        return render(request, "degree_add.html", {
            'form': form,'titlehead': 'Teacher Avaluation',
		'pagetitle': 'Evaluacio de docencia',
        },context_instance = RequestContext(request))	

def subject_add (request):
	if request.method == 'POST':
            form = AddSubject(request.POST)
            if form.is_valid():
              new_subject = form.save()
	      return HttpResponseRedirect('/subjects/')
        else:
            form = AddSubject
        return render(request, "subject_add.html", {
            'form': form,'titlehead': 'Teacher Avaluation',
		'pagetitle': 'Evaluacio de docencia',
        },context_instance = RequestContext(request))	

def teacher_add (request):
	if request.method == 'POST':
            form = AddTeacher(request.POST)
            if form.is_valid():
              new_teacher = form.save()
	      return HttpResponseRedirect('/teachers/')
        else:
            form = AddTeacher
        return render(request, "teacher_add.html", {
            'form': form,'titlehead': 'Teacher Avaluation',
		'pagetitle': 'Evaluacio de docencia',
        },context_instance = RequestContext(request))	

def personal_data(request):
	variables = Context({
		'titlehead': 'Teacher Avaluation',
		'pagetitle': 'Evaluacio de docencia',
		'contentbody': 'Menu Personal:',
		})
	context_instance = RequestContext(request)
	return render_to_response('personal_data.html',variables,context_instance)

def logoutPage(request):
	logout(request)
	variables = Context({
		'titlehead': 'Log out',
		'contentbody': 'Has tancat la sessio.',
		})

	context_instance = RequestContext(request)
	return render_to_response('mainpage.html',variables,context_instance)
