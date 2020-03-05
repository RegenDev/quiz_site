from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect


def FrontPageView(request):
	return render(request, 'home.html')
     #return HttpResponse("Hello, world. You're at the polls index.")
