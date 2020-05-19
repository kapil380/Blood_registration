from django.db import models
class Register(models.Model):
    Donor_name=models.CharField(max_length=100)
    Contact_no=models.IntegerField()
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Blood_group=models.CharField(max_length=100)
    Rh_factor=models.CharField(max_length=100)
    blood_amt=models.CharField(max_length=100)
    Address=models.TextField()



