from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def homepage(request):
    return render(request, 'home/homepage.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        errors = []
        if not email:
            errors.append('Email is required.')
        if not password:
            errors.append('Password is required.')

        if User.objects.filter(username=email).exists():
            errors.append('An account with that email already exists.')

        if errors:
            return render(request, 'home/signup.html', {'errors': errors, 'form': {'first_name': first_name, 'last_name': last_name, 'email': email}})
        # create user
        user = User(username=email, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        return redirect('login')

    return render(request, 'home/signup.html')

def login_view(request):
    # render-only login page; add auth handling later as needed
    return render(request, 'home/login.html')
