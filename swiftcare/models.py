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

    def __str__(self):
            return f"{self.doctor_name}"





