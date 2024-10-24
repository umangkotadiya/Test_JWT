from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user model
class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    other_details = models.TextField()
    is_management = models.BooleanField()
    management_type = models.CharField(max_length=100,default="Patient") 

    def __str__(self):
        return self.email


class Hospital(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField()

    def __str__(self):
        return self.name
        

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Appointment(models.Model):
    pass
    # patient = models.ForeignKey(User, on_delete=models.CASCADE)
    # doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    # appointment_date = models.DateTimeField()
    # reason = models.TextField()
    # status = models.CharField(max_length=50, default='Scheduled')

    # def __str__(self):
    #     return f"Appointment with {self.doctor.name} on {self.appointment_date}"


