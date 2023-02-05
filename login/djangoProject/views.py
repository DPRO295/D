from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            return render(request, 'logins.html', {'error_message': 'Invalid login'})
    return render(request, 'logins.html')

def welcome_view(request):
    return render(request, 'welcome.html')