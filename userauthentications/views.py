from django.shortcuts import render, redirect
from userauthentications.forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import logout
from userauthentications.models import User

# User = settings.AUTH_USER_MODEL


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, your account was created!")
            
            # Authenticate and login the user
            new_user = authenticate(username=form.cleaned_data['email'], 
                                    password=form.cleaned_data['password1'])
            if new_user is not None:
                login(request, new_user)
                return redirect("core:index")
            else:
                messages.error(request, "Authentication failed. Please try again.")
    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'userauths/sign-up.html', context)

def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect("core:index")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "you are logged in.")
                return redirect("core:index")
            else:
                messages.warning(request, "User Does not exist, create an account.")
        except:
            messages.warning(request, f"User with email {email} does not exist.")
        

    return render(request, "userauths/sign-in.html")


def logout_view(request):
    logout(request)
    messages.success(request, "you are logged out.")
    return redirect("userauthentications:sign-in")