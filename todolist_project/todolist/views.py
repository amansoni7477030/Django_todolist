# todolist/views.py
from django.shortcuts import render
from .models import Task
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todolist/task_list.html', {'tasks': tasks})
