from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.conf import settings

User = get_user_model()

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("last_name", "first_name","username", "email", "employee_number", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 社員番号の初期値を現在の最大値+1に設定
        self.fields['employee_number'].initial = User.get_next_employee_number()