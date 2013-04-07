from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def mainpage(request):
	template = get_template('mainpage.html')
	variables = Context({
		'titlehead': 'Teacher Avaluation',
		'pagetitle': 'Evaluacio de docencia',
		'contentbody': 'Benvinguts a el aplicatiu de evaluacio de docencia , navega pel menu per veure el llistat de les diferents entitats.'

		})
	output = template.render(variables)
	return HttpResponse(output)

