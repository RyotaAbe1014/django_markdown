from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic import TemplateView

app_name = "registration"

urlpatterns = [
    path("signup-done/", TemplateView.as_view(template_name="registration/signup_done.html"), name = "signup_done"),
]
