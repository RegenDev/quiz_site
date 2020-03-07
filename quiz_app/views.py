from django.shortcuts import render
from .models import Question
from .models import QuizTip

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect


def FrontPageView(request):
	return render(request, 'home.html')

def AboutView(request):
	return render(request, 'about.html')

def QuizView(request):
	questions = Question.objects.all()
	return render(request, 'quiz.html', locals())

#MORE VIEWS
#----Game Categories
#----ALl Quiz Tips
