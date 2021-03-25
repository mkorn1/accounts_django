from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import SignUpForm

def home(request):
    # return HttpResponse('Hello, World! \nthis is the homepage!')
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
