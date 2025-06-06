from django.urls import path
from .views import auth_register_login

app_name = "user"

urlpatterns = [
    path("", auth_register_login, name="auth_register_login"),
]