from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'signup.html')

def login_page(request):
    return render(request,'login.html')
