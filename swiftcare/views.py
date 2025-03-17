from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from swiftcare.models import Patient,Doctor, Medicine
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
            return redirect('homepage')  # Redirect to the home page after successful login
    else:
        form = CustomLoginForm()

    return render(request, 'login.html',{'form':form})


@login_required(login_url='login')
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
    return render(request,'patient_details.html')


def doctor_details(request):
    if request.method == 'POST':
        doctor_name = request.POST.get('doctor_name')
        doctor_email = request.POST.get('doctor_email')
        doctor_contact = request.POST.get('doctor_contact')
        doctor_specialization = request.POST.get('doctor_specialization')
        doctor_availability = request.POST.get('doctor_availability')
        doctor_image = request.FILES.get('doctor_image')

        doctor = Doctor(
            doctor_name=doctor_name,
            doctor_email=doctor_email,
            doctor_contact=doctor_contact,
            doctor_specialization=doctor_specialization,
            doctor_availability=doctor_availability,
            doctor_image=doctor_image
        )
        doctor.save()


    return render(request,'doctors_details.html')




def view_doctors(request):
    doctors = Doctor.objects.all()
    return render(request,'doctors.html',{'doctors':doctors})


@login_required(login_url='login')
def registered_patients(request):
    patients = Patient.objects.all()
    return render(request,'registered_patients.html',{'patients':patients})

def pharmacy(request):
    medicines = Medicine.objects.all()
    return render(request, 'pharmacy.html',{'medicines':medicines})

def medicine(request):
    if request.method == 'POST':
        medicine_name = request.POST.get('medicine_name')
        medicine_quantity = request.POST.get('medicine_quantity')
        medicine_category = request.POST.get('medicine_category')
        medicine_prescription = request.POST.get('medicine_prescription')
        medicine_duration = request.POST.get('medicine_duration')
        medicine_price = request.POST.get('medicine_price')
        medicine_image = request.FILES.get('medicine_image')

        medicine = Medicine(
            medicine_name=medicine_name,
            medicine_quantity=medicine_quantity,
            medicine_category=medicine_category,
            medicine_prescription=medicine_prescription,
            medicine_duration=medicine_duration,
            medicine_price=medicine_price,
            medicine_image=medicine_image

        )
        medicine.save()

    return render(request, 'medicine.html')




