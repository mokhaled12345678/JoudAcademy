from django.shortcuts import render
from .models import Course, Home
from django.core.mail import send_mail
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import NewUserForm

# Create your views here.
def home(request):
    Courses = Course.objects.all()
    homes = Home.objects.all()
    return render(request, 'UserView/home.html', {'courses':Courses, 'homes':homes})

def courses(request):
    Courses = Course.objects.all()
    return render(request, 'UserView/Courses-and-Fees.html', {'courses':Courses})

def faq(requset):
    Courses = Course.objects.all()
    return render(requset, 'UserView/FAQ.html', {'courses':Courses})

def login_user(request):
    page = 'login'
    courses = Course.objects.all()
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
            authenticated_user = authenticate(request, username=email, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('home')
            else:
                messages.error(request, "Incorrect password")
        except User.DoesNotExist:
            messages.error(request, "User does not exist")
    
    return render(request, 'UserView/Registration-and-Fees.html', {'page': page,  'messages': messages.get_messages(request), 'courses':courses})

def logoutUser(request):
    logout(request)
    return redirect('home')

def register(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']  # Add this line to get the username
            phone = form.cleaned_data['phone_number']
            # Use the custom user model manager to create the user
            User = get_user_model()  # Get the custom user model
            user = User.objects.create_user(username=username, phone_number=phone, email=email, password=password)  # Pass the username
            
            # Authenticate and login the user
            authenticated_user = authenticate(request, username=email, password=password)  # Pass the username
            print(authenticated_user)
            if authenticated_user:
                login(request, authenticated_user)
                return redirect('home')  # Redirect to the 'home' URL
    else:
        form = NewUserForm()

    return render(request, 'UserView/Registration-and-Fees.html', {'form': form, 'courses':courses})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        data = {'name':name,
                'email':email,
                'subject':subject,
                "message":message}

        message = '''
                New Message: {}


                From: {}
                '''.format(data['message'], data['email'])
        # Send email
        send_mail(data['subject'], message, '', ['mohammedkhaledmali888@gmail.com'])
    Courses = Course.objects.all()
    return render(request, 'UserView/Contact-Us.html', {'courses':Courses})

def about(request):
    Courses = Course.objects.all()
    return render(request, 'UserView/About-us.html', {'courses':Courses})

def course(request, pk):
    course=Course.objects.get(id=pk)
    return render(request, 'UserView/course.html', {'course':course})

def char(request):
    return render(request, 'UserView/char.html')