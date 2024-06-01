from pyexpat.errors import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from . import urls
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')

        print(f"Username: {username}, Password: {pass1}")

        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('loggedHomepage')
        else:
            return render(request, "accounts/login.html", {'error': 'Invalid Credentials'})

    return render(request, "accounts/login.html")


def user_register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        print(f"Username: {uname}, Password: {pass1}")

        if pass1 != pass2:
            return render(request, "accounts/register.html", {'error': 'Passwords do not match'})
        elif User.objects.filter(username=uname).exists():
            messages.error(request, "This username is already taken")
            return render(request, "accounts/register.html", {'error': 'Username is taken'})
        else:
            user_manu = User.objects.create_user(uname, email, pass1)
            user_manu.save()

            return redirect('login')

    return render(request, "accounts/register.html")


def log_out(request):
    logout(request)
    return redirect("login")


@login_required
def user_profile(request):
    user = request.user
    context = {
        'username': user.username,
        'email': user.email,
    }
    return render(request, 'accounts/view_profile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        new_username = request.POST.get('new_username')
        new_email = request.POST.get('new_email')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Validate and update the username
        if new_username:
            user.username = new_username
            user.save()

        # Validate and update the email
        if new_email:
            user.email = new_email
            user.save()

        # Validate and update the password
        if new_password and confirm_password and new_password == confirm_password:
            user.set_password(new_password)
            user.save()
            # Update the session to prevent logouts
            update_session_auth_hash(request, user)

        return redirect('profile')

    return render(request, 'accounts/edit_profile.html')
