from django.db import models


class Patient(models.Model):
    filled_at=models.DateTimeField(auto_now_add=True)
    patient_name = models.CharField(max_length=100)
    patient_dob = models.DateField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    patient_gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='M')
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    patient_bloodGroup = models.CharField(max_length=3, choices= BLOOD_GROUP_CHOICES, default='O+')
    patient_disability = models.CharField(max_length=50)
    patient_contact = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.patient_name}"


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    doctor_email = models.EmailField()
    doctor_contact = models.CharField(max_length=50)

    SPECIALIZATION_CHOICES = [
        ('Cardiology', 'Cardiology'),
        ('Radiology', 'Radiology'),
        ('Neurology', 'Neurology'),
        ('Mental Health', 'Mental Health'),
        ('Oncology', 'Oncology'),
        ('Osteology', 'Osteology'),

    ]
    doctor_specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES, default='cardiology')

    AVAILABILITY_CHOICES = [
        ('7am-1pm', '7am-1pm'),
        ('1pm-6pm', '1pm-6pm'),
        ('6pm-9pm', '6pm-9pm'),
        ('9pm-7am', '9pm-7am'),

    ]
    doctor_availability = models.CharField(max_length=50, choices=AVAILABILITY_CHOICES, default='7am-1pm')
    doctor_image = models.ImageField(upload_to='doctors/')


    def __str__(self):
            return f"{self.doctor_name}"



class Medicine(models.Model):
    medicine_name = models.CharField(max_length=100)
    medicine_quantity = models.IntegerField()

    CATEGORY_CHOICES = [
        ('Antibiotics', 'Antibiotics'),
        ('Painkillers', 'Painkillers'),
        ('Antivirals', 'Antivirals'),
        ('Antiseptics', 'Antiseptics'),
        ('Vaccine', 'Vaccine'),
        ('Vitamin', 'Vitamin'),

    ]
    medicine_category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Antibiotics')

    PRESCRIPTION_CHOICES = [
        ('1×3', '1×3'),
        ('2×3', '2×3'),
        ('2×2', '2×2'),
        ('5ml×2', '5ml×2'),
        ('5ml×3', '5ml×3'),
        ('10ml×2', '10ml×2'),
        ('10ml×3', '10ml×3'),

    ]
    medicine_prescription = models.CharField(max_length=50, choices=PRESCRIPTION_CHOICES, default='1×3')

    DURATION_CHOICES = [
        ('5 weeks', '5 weeks'),
        ('4 weeks', '4 weeks'),
        ('3 weeks', '3 weeks'),
        ('2 weeks', '2 weeks'),
        ('1 week', '1 week'),

    ]
    medicine_duration = models.CharField(max_length=50, choices=DURATION_CHOICES, default='5 weeks')

    medicine_image = models.ImageField(upload_to='medicines/')
    medicine_price = models.IntegerField()



    def __str__(self):
            return f"{self.medicine_name}"

class Appointment(models.Model):
    APPOINTMENT_TYPES = [
        ('Physical', 'Physical'),
        ('Virtual', 'Virtual'),
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    appointment_type = models.CharField(max_length=10, choices=APPOINTMENT_TYPES, default='Physical')  # New field



    def __str__(self):
        return f"Appointment with {self.doctor.doctor_name} - {self.name}"


class Transaction(models.Model):
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    mpesa_receipt_number = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    transaction_date = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return f"Transaction {self.mpesa_receipt_number or self.transaction_id} - {self.status}"
