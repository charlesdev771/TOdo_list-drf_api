from app.views import TodoDetailChangeAndDelete, TodoListCreate
from django.urls import path 

urlpatterns = [
    path('', TodoListCreate.as_view()),
    path('<int:pk>/', TodoDetailChangeAndDelete.as_view()),
]
