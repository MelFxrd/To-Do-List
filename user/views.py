from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def auth_register_login(request):
    if request.method == "POST":
        if "login" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("task_list")

        elif "register" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, password=password)
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect("task_list")

    return render(request, "auth.html")