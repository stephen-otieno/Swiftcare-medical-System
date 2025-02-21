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
        return self.patient_name
