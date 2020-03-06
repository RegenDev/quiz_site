from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect


def FrontPageView(request):
	return render(request, 'home.html')

def AboutView(request):
	return render(request, 'about.html')

def QuizView(request, question_id):
	questions = get_object_or_404(Question, pk=question_id)
	return render(request, 'quiz.html', {'question': question})

#MORE VIEWS
#----Game Categories
#----ALl Quiz Tips
