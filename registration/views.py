from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.shortcuts import render
from .forms import SignUpForm
from .mixins import SuperuserRequiredMixin
User = get_user_model()

class SignUpView(SuperuserRequiredMixin, CreateView):
    form_class = SignUpForm
    # サインアップ成功時に遷移する画面
    success_url = reverse_lazy('registration:signup_done')
    template_name = 'registration/signup.html'

