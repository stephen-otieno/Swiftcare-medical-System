from django.shortcuts import render,redirect
from swiftcare.models import Client


# Create your views here.

def homepage(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        client_name = request.POST['client_name']
        client_email = request.POST['client_email']
        client_password1 = request.POST['client_password1']
        client_password2 = request.POST['client_password2']

        client = Client(
            client_name= client_name,
            client_email= client_email,
            client_password1= client_password1,
            client_password2= client_password2
        )

        client.save()
        return redirect('homepage')


    return render(request,'signup.html')

def login_page(request):
    return render(request,'login.html')
