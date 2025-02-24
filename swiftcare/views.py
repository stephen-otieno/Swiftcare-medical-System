from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from swiftcare.models import Patient,Doctor
from django.contrib import messages
from .forms import RegisterForm,CustomLoginForm




# Create your views here.



def homepage(request):
    return render(request,'index.html')


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
    else:
        form = RegisterForm()





    return render(request, 'signup.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('details')  # Redirect to the home page after successful login
    else:
        form = CustomLoginForm()

    return render(request, 'login.html',{'form':form})


def patient_details(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        patient_dob = request.POST.get('patient_dob')
        patient_gender = request.POST.get('patient_gender')
        patient_bloodGroup = request.POST.get('patient_bloodGroup')
        patient_disability = request.POST.get('patient_disability')
        patient_contact = request.POST.get('patient_contact')

        patient=Patient(
            patient_name=patient_name,
            patient_dob=patient_dob,
            patient_gender=patient_gender,
            patient_bloodGroup=patient_bloodGroup,
            patient_disability=patient_disability,
            patient_contact=patient_contact
        )

        patient.save()
        # return redirect('patient_details')



    return render(request,'patient_details.html')


def doctor_details(request):
    if request.method == 'POST':
        doctor_name = request.POST.get('doctor_name')
        doctor_email = request.POST.get('doctor_email')
        doctor_contact = request.POST.get('doctor_contact')
        doctor_specialization = request.POST.get('doctor_specialization')
        doctor_availability = request.POST.get('doctor_availability')

        doctor = Doctor(
            doctor_name=doctor_name,
            doctor_email=doctor_email,
            doctor_contact=doctor_contact,
            doctor_specialization=doctor_specialization,
            doctor_availability=doctor_availability
        )
        doctor.save()


    return render(request,'doctors_details.html')


