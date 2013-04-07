from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def mainpage(request):
	template = get_template('mainpage.html')
	variables = Context({
		'titlehead': 'Teacheravaluation aPP',
		'pagetitle': 'Welcome to the Teacheravaluation aPPlication',
		'contentbody': 'OLA KE ASE'

		})
	output = template.render(variables)
	return HttpResponse(output)

