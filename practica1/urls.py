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
    url(r'^teachers/(?P<teacher_id>\w+)/$', singular_teacher),
    
    # Degrees:
    url(r'^degrees/$', degree, name='degrees'),
    url(r'^degrees/(?P<degree_id>\w+)/$', singular_degree ),

    # Subjects:
    url(r'^subjects/$', subject, name='subjects'),
    url(r'^subjects/(?P<subject_id>\w+)/$', singular_subject ),

    # Evaluations:
    url(r'^evaluations/$', evaluation, name='evaluations'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Login & Register
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logoutPage),
    url(r'^registration/$', registration),
)

