from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect


def FrontPageView(request):
	return render(request, 'home.html')

def AboutView(request):
	return render(request, 'about.html')

def QuizView(request):
	return render(request, 'quiz.html')
