from django.db import models
from Admin.models import *

# Create your models here.
class tbl_userreg(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_address=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    user_photo=models.FileField(upload_to="Assets/UserDocs/")
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
class tbl_recruiter(models.Model):
    recruiter_name=models.CharField(max_length=50)
    recruiter_email=models.CharField(max_length=50)
    recruiter_password=models.CharField(max_length=50)
    recruiter_address=models.CharField(max_length=50)
    recruiter_status=models.IntegerField(default=0)
    recruiter_contact=models.CharField(max_length=50)
    recruiter_photo=models.FileField(upload_to="Assets/Recruiterdocs/Photo/")
    recruiter_proof=models.FileField(upload_to="Assets/Recruiterdocs/Proof/")
    recruiter_licence=models.FileField(upload_to="Assets/Recruiterdocs/Licence/")
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
