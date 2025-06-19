from django.urls import path
from .views import task_list, edit_task
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", task_list, name="task_list"),
    path("edit/<int:task_id>/", edit_task, name="edit_task"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
]