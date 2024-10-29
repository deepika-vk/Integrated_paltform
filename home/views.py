from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import FeedbackForm
def about(request):
    return render(request,'about.html')
def home(request):
    return render(request,'home.html')
def problems(request):
    return render(request,'Problems.html')
def log_in(request):
    if request.user.is_authenticated:
            return render(request,'404.html')
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            context={'greenalert':"login successful"}
            return render(request,'home.html',context)
        if User.objects.filter(username=username).exists():
            context={'redalert':"wrong password"}
            return render(request,'login.html',context)
        context={'redalert':"User name doesn't exist"}
        return render(request,'login.html',context)
    else:
        return render(request,'login.html')
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        context={'greenalert':"logout successful"}
        return render(request,'home.html',context)
    return render(request,'404.html')

def contact_us(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your feedback has been submitted successfully.')
            return redirect('contact_us')  # Redirect after successful submission
    else:
        form = FeedbackForm()
    
    return render(request, 'contact_us.html', {'form': form})


def register_page(request):
    if request.user.is_authenticated:
        return render(request, '404.html')

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            context = {'redalert': 'Username already taken'}
            return render(request, 'register.html', context)

        # Create the user with first name, last name, and password
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.save()

        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('login')

    return render(request, 'register.html')
