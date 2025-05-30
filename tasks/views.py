from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all().order_by('deadline', 'priority')
    return render(request, "tasks/task_list.html", {"tasks": tasks})