from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def task_list(request):
    if request.method == "POST" and "create_task" in request.POST:
        title = request.POST.get("title", "")
        description = request.POST.get("description", "")
        priority = request.POST.get("priority", "1")
        deadline = request.POST.get("deadline", "")

        if title:
            task = Task(
                user=request.user,
                title=title,
                description=description,
                priority=int(priority),
                created_at=timezone.now(),
                updated_at=timezone.now()
            )
            if deadline:
                task.deadline = deadline
            task.save()
        return redirect("tasks:task_list")

    if request.method == "POST" and "delete_task" in request.POST:
        task_id = request.POST.get("delete_task")
        try:
            task = Task.objects.get(id=int(task_id), user=request.user) 
            task.delete()
        except Task.DoesNotExist:
            pass
        return redirect("tasks:task_list")

    tasks = Task.objects.filter(user=request.user).order_by("deadline", "-priority")
    return render(request, "task_list.html", {"tasks": tasks})