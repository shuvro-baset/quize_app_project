from django.urls import path
from .views import QuizListView, quizView

app_name = 'quizeApp'

urlpatterns = [
    path('', QuizListView.as_view(), name='main-view'),
    path('<pk>/', quizView, name='quiz-view'),
]