from django.shortcuts import render, redirect
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def task_list(request):
    if request.method == "POST":
        if "create_task" in request.POST:
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
            return redirect("task_list")
        
        if "delete_task" in request.POST:
            task_id = request.POST.get("delete_task")
            Task.objects.filter(id=task_id, user=request.user).delete()
            return redirect("task_list")

        if "complete_task" in request.POST:
            task_id = request.POST.get("complete_task")
            try:
                task = Task.objects.get(id=task_id, user=request.user)
                task.is_completed = True
                task.save()
            except Task.DoesNotExist:
                pass
            return redirect("task_list")

    tasks = Task.objects.filter(user=request.user).order_by("is_completed", "deadline", "-priority")
    return render(request, "task_list.html", {"tasks": tasks})