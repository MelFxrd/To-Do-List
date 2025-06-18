from django.urls import path
from .views import task_list, edit_task

urlpatterns = [
    path("", task_list, name="task_list"),
    path("edit/<int:task_id>/", edit_task, name="edit_task"),
]