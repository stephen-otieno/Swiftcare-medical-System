from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from swiftcare.models import Patient,Doctor,Medicine,Appointment,Transaction
from django.contrib import messages
from .forms import RegisterForm,CustomLoginForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime
from django.core.mail import send_mail
import requests
import base64
import json






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




@login_required(login_url="login")
def view_doctors(request):
    doctors = Doctor.objects.all()
    return render(request,'doctors.html',{'doctors':doctors})


@login_required(login_url='login')
def registered_patients(request):
    patients = Patient.objects.all()
    return render(request,'registered_patients.html',{'patients':patients})
@login_required(login_url="login")
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


def appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)  # Fetch doctor by ID

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        date = request.POST.get("date")
        time = request.POST.get("time")
        appointment_type = request.POST.get("appointment_type")
        reason = request.POST.get("reason")

        if name and email and date and time:  # Ensure all fields are provided
            appointment = Appointment(
                doctor=doctor,  # Associate with the selected doctor
                name=name,
                email=email,
                date=date,
                time=time,
                appointment_type=appointment_type,
                reason=reason
            )
            appointment.save()

            # Add success message
            messages.success(request, "Your appointment has been scheduled successfully!")

            # Redirect to prevent form resubmission on page refresh
            return redirect('book_appointment', doctor_id=doctor_id)

    return render(request, "appointment.html", {"doctor": doctor})


def scheduled_appointments(request):
    appointments = Appointment.objects.select_related("doctor").all().order_by("date", "time")
    return render(request, "scheduled_appointments.html", {"appointments": appointments})



# Mpesa stk push

def pay(request):
    return render(request,'pay.html')


def payment_cancelled(request):
    return render(request, 'payment_cancelled.html')

def payment_failed(request):
    return render(request, 'payment_failed.html')


def payment_success(request):
    return render(request, 'payment_success.html')


def waiting_page(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    return render(request, 'waiting.html', {'transaction_id': transaction_id})


class MpesaPassword:
    @staticmethod
    def generate_security_credential():
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

        business_short_code = '174379'
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        data_to_encode = business_short_code + passkey + timestamp
        online_password = base64.b64encode(data_to_encode.encode()).decode('utf-8')

        return online_password


CONSUMER_KEY = 'xNeRioGer58j1EQHkxJ2oZLDJ1v5HqqAoXt8Si1gH1tQpJXv'
CONSUMER_SECRET = 'WsZ4Vl2g0J7aWmDc4gkfewOl9ZlyUm2ke2fQtONGOROMUFIR6FAVdhZv1wcGyxiS'
SHORTCODE = '174379'
PASSKEY = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
BASE_URL = 'https://sandbox.safaricom.co.ke'




def generate_access_token():
    auth_url = f'{BASE_URL}/oauth/v1/generate?grant_type=client_credentials'
    response = requests.get(auth_url, auth=(CONSUMER_KEY, CONSUMER_SECRET))
    return response.json().get('access_token')



@csrf_exempt
def stk_push(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        amount = request.POST.get('amount')
        name = request.POST.get('name')
        email = request.POST.get('email')

        transaction = Transaction.objects.create(
            phone_number=phone,
            amount=amount,
            status="Pending",
            description="Awaiting callback",
            name=name,
            email=email,
        )

        access_token = generate_access_token()
        stk_url = f'{BASE_URL}/mpesa/stkpush/v1/processrequest'
        headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}

        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        password = base64.b64encode(f'{SHORTCODE}{PASSKEY}{timestamp}'.encode()).decode()

        payload = {
            "BusinessShortCode": SHORTCODE,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": SHORTCODE,
            "PhoneNumber": phone,
            "CallBackURL": "https://b6ec-217-199-146-223.ngrok-free.app/callback",
            "AccountReference": f"Transaction_{transaction.id}",
            "TransactionDesc": "Payment for services"
        }

        response = requests.post(stk_url, json=payload, headers=headers)
        response_data = response.json()

        transaction_id = response_data.get('CheckoutRequestID', None)
        transaction.transaction_id = transaction_id
        transaction.description = response_data.get('ResponseDescription', 'No description')
        transaction.save()

        return redirect('waiting_page', transaction_id=transaction.id)

    return JsonResponse({"error": "Invalid request"}, status=400)



def check_status(request, transaction_id):
    transaction = Transaction.objects.filter(id=transaction_id).first()

    if not transaction:
        return JsonResponse({"status": "Failed", "message": "Transaction not found"}, status=404)

    if transaction.status == "Success":
        return JsonResponse({"status": "Success", "message": "Payment Successful"})
    elif transaction.status == "Failed":
        return JsonResponse({"status": "Failed", "message": "Payment Failed"})
    elif transaction.status == "Cancelled":
        return JsonResponse({"status": "Cancelled", "message": "Transaction was cancelled by the user"})
    else:
        return JsonResponse(
            {"status": "Unknown", "message": "Transaction is still being processed or status is unknown"})





@csrf_exempt
def callback(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Invalid request method"}, status=400)

    try:
        data = json.loads(request.body)
        print("Received callback data:", data)

        stk_callback = data.get('Body', {}).get('stkCallback', {})
        result_code = stk_callback.get('ResultCode')
        result_desc = stk_callback.get('ResultDesc', '')
        transaction_id = stk_callback.get('CheckoutRequestID')

        if not transaction_id:
            print("Missing transaction ID in callback")
            return JsonResponse({"error": "Missing transaction ID"}, status=400)

        transaction = Transaction.objects.filter(transaction_id=transaction_id).first()
        if not transaction:
            print(f"Transaction {transaction_id} not found.")
            return JsonResponse({"error": "Transaction not found"}, status=404)

        if result_code == 0:
            callback_metadata = stk_callback.get('CallbackMetadata', {}).get('Item', [])
            receipt_number = next((item.get('Value') for item in callback_metadata if item.get('Name') == 'MpesaReceiptNumber'), None)
            amount = next((item.get('Value') for item in callback_metadata if item.get('Name') == 'Amount'), None)
            transaction_date_str = next((item.get('Value') for item in callback_metadata if item.get('Name') == 'TransactionDate'), None)

            transaction_date = datetime.strptime(str(transaction_date_str), "%Y%m%d%H%M%S") if transaction_date_str else None

            transaction.mpesa_receipt_number = receipt_number
            transaction.transaction_date = transaction_date
            transaction.amount = amount
            transaction.status = "Success"
            transaction.description = "Payment successful"
            transaction.save()

            print(f"Transaction {transaction_id} updated successfully.")

            # Send confirmation email
            if transaction.email:
                subject = "Payment Receipt Confirmation"
                message = f"""
                Dear {transaction.name},

                Thank you for your payment of {transaction.amount}.
                Your Mpesa transaction code is {transaction.mpesa_receipt_number}.

                Should you have any questions, please contact us:
                Phone: 0115598800
                Powered by Stemiot Innovations (https://stemiotsoftwares.onrender.com/)

                Best regards,
                Stemiot Innovations
                """
                html_message = f"""
                <p>Dear {transaction.name},</p>
                <p>Thank you for your payment of {transaction.amount}.</p>
                <p>Your receipt number is <strong>{transaction.mpesa_receipt_number}</strong>.</p>
                <p>Should you have any questions, please feel free to reach us at:</p>
                <p><strong>Phone:</strong> 0115598800</p>
                <p>Powered by <a href='https://stemiotsoftwares.onrender.com/' target='_blank'>Stemiot Innovations</a></p>
                <p>Best regards,<br>Stemiot Innovations</p>
                """
                send_mail(
                    subject,
                    message,
                    'engineerotienoduor14@gmail.com',
                    [transaction.email],
                    fail_silently=False,
                    html_message=html_message,
                )
                print("Payment receipt email sent.")

        elif result_code == 1:
            transaction.status = "Failed"
            transaction.description = result_desc
            transaction.save()
            print(f"Transaction {transaction_id} failed: {result_desc}")

        elif result_code == 1032:
            transaction.status = "Cancelled"
            transaction.description = "Transaction cancelled by user"
            transaction.save()
            print(f"Transaction {transaction_id} cancelled.")

        else:
            print(f"Unhandled ResultCode: {result_code} - {result_desc}")
            transaction.status = "Unknown"
            transaction.description = f"Unhandled status: {result_desc}"
            transaction.save()

        return JsonResponse({"message": "Callback processed successfully"}, status=200)

    except json.JSONDecodeError:
        print("Invalid JSON data received")
        return JsonResponse({"error": "Invalid JSON format"}, status=400)
    except Exception as e:
        print(f"Error processing callback: {e}")
        return JsonResponse({"error": "Internal server error"}, status=500)

