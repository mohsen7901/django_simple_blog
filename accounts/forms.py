from django.forms import EmailField, EmailInput
# from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField


class MyUserCreationForm(UserCreationForm):
    captcha = CaptchaField()
    email = EmailField(max_length=100, widget=EmailInput)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'captcha')
