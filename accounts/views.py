from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import MyUserCreationForm
from accounts.backends import EmailOrUsernameModelBackend
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid(): 
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            user_obj = EmailOrUsernameModelBackend()
            user = user_obj.authenticate(request, username, password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                msg = "The entered Username/Email or Password not found! Try entering them again."
                messages.add_message(request, level=messages.ERROR, message=msg)
        else:
            msg = "your Username/Email or Password don't match or exist. Try again."
            messages.add_message(request, messages.ERROR, msg)
        
    form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    else:
        logout(request)
        msg = "You have logged out successfully!"
        messages.add_message(request, level=messages.SUCCESS, message=msg)
        return redirect('/')
    
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            msg = "Your account has been created successfully! Please login."
            messages.add_message(request, level=messages.SUCCESS, message=msg)
            return redirect('/accounts/login')
        else:
            msg = "Entered data is invalid! Try again."
            messages.add_message(request, level=messages.ERROR, message=msg)
    
    form = MyUserCreationForm()
    context = {'form':form}
    return render(request, 'accounts/signup.html', context=context)

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_message = """We've emailed you instructions for resetting your password,  
                      if an account exists with the email you entered, You should receive them shortly. 
                      If you don't receive an email,  
                      please make sure you've entered the address you registered with, and check your spam folder."""
    success_url = reverse_lazy('website:index')


