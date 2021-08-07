from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
# Create your views here.

class QuizListView(ListView):
    model = Quiz
    template_name = 'main.html'

def quizView(requst, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(requst, 'quiz.html', {'obj': quiz})