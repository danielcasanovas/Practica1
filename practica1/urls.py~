from django.conf.urls import patterns, include, url 
from teacherAvaluation.views import *
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', mainpage, name='home'),
    #url(r'^practica1/', include('practica1.foo.urls')),

    # Teachers:
    url(r'^teachers/$', teacher, name='teachers'),
    url(r'^teachers/add/$', teacher_add, name='add_teacher'),
    url(r'^teachers/edit/(?P<teacher_id>\w+)/$', teacher_edit, name='edit_teacher'),
    url(r'^teachers/update/(?P<teacher_id>\w+)/$', teacher_update, name='update_teacher'),
    url(r'^teachers/delete/(?P<teacher_id>\w+)/$', teacher_delete, name='delete_teacher'),
    url(r'^teachers/(?P<teacher_id>\w+)/$', singular_teacher),
    url(r'^teachers/review/(?P<teacher_id>\w+)/$', review, name='create review'),
    
    # Degrees:
    url(r'^degrees/$', degree, name='degrees'),
    url(r'^degrees/add/$', degree_add, name='add_degree'),
    url(r'^degrees/edit/(?P<degree_id>\w+)/$', degree_edit, name='edit_degree'),
    url(r'^degrees/update/(?P<degree_id>\w+)/$', degree_update, name='update_degree'),
    url(r'^degrees/delete/(?P<degree_id>\w+)/$', degree_delete, name='delete_degree'),
    url(r'^degrees/(?P<degree_id>\w+)/$', singular_degree ),
    

    # Subjects:
    url(r'^subjects/$', subject, name='subjects'),
    url(r'^subjects/add/$', subject_add, name='add_subjects'), 
    url(r'^subjects/edit/(?P<subject_id>\w+)/$', subject_edit, name='edit_subject'),
    url(r'^subjects/update/(?P<subject_id>\w+)/$', subject_update, name='update_subject'),   
    url(r'^subjects/delete/(?P<subject_id>\w+)/$', subject_delete, name='delete_subject'),
    url(r'^subjects/(?P<subject_id>\w+)/$', singular_subject ),
    

    # Evaluations:
    url(r'^evaluations/$', evaluation, name='evaluations'),
    url(r'^evaluations/add/$', evaluation_add, name='add_evaluations'),
    url(r'^evaluations/edit/(?P<evaluation_id>\w+)/$', evaluation_edit, name='edit_evaluation'),
    url(r'^evaluations/update/(?P<evaluation_id>\w+)/$', evaluation_update, name='update_evaluation'),   
    url(r'^evaluations/delete/(?P<evaluation_id>\w+)/$', evaluation_delete, name='delete_evaluation'),
    url(r'^evaluations/(?P<evaluation_id>\w+)/$', singular_evaluation),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Login & Register
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logoutPage),
    url(r'^registration/$', registration),
    url(r'^personalData/$', personal_data),
    url(r'^personalData/pwd/$', personal_data_changepsword_edit),
    url(r'^personalData/update/$', personal_data_changepsword_update),
)

