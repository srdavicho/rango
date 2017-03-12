from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
# 	return HttpResponse("Rango says hey there partner!<br/><a href='/rango/about'>About</a>")

def index(request):
	
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

	return render(request, 'rango/index.html', context=context_dict)

def about(request):
	
	context = {
		'myname': "David Gaudreault",
	}

	return render(request, 'rango/about.html', context=context)
