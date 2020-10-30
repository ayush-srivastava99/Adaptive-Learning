from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "quizzes"

urlpatterns = [
    path('createassignment/',createAssignment,name="cassgn"),
    path('quizhome/',QuizHome,name='qhome'),
    path('quizmain/',QuizMain,name='qmain'),
    path('submitAssignment/',submitAssignment,name='sassgn'),
    path('takequiz/<int:quiz_id>/', takequiz, name='takequiz'),
    path('storeresult', storeresult, name='storeresult'),
    path('addquestion/<int:quiz_id>/', addquestion, name='addquestion'),
    path('assignstu', assignstu, name='assignstu'),
]