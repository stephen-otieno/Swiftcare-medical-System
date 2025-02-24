# Generated by Django 5.1.3 on 2025-02-21 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swiftcare', '0004_patient_patient_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_bloodGroup',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], default='Select Blood Group', max_length=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='Select Gender', max_length=10),
        ),
    ]
