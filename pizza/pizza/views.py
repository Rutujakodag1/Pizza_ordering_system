from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'index.html')

def menu(request):
    return render(request,'menu.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')

def blog(request):
    return render(request,'blog.html')

def blog_single(request):
    return render(request,'blog-single.html')

# def send_email(request):
#     return render(request,'send_email.php')

# views.py

# def order_success(request):
#     return HttpResponse('order placed successfuly')   

def login_view(request):
    return render(request,'login.html')


def login_submit(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a success page.
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    return redirect('login')
