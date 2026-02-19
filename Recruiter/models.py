from django.db import models
from Admin.models import*
from Guest.models import*

# Create your models here.
class tbl_job(models.Model):
    job_title=models.CharField(max_length=50)
    job_details=models.CharField(max_length=50)
    job_lastdate=models.DateField()
    job_date=models.DateField(auto_now_add=True)
    job_experience=models.CharField(max_length=50)
    job_requirment=models.CharField(max_length=50)
    jobtype=models.ForeignKey(tbl_jobtype,on_delete=models.CASCADE)
    jobcategory=models.ForeignKey(tbl_jobcategory,on_delete=models.CASCADE)
    recruiter=models.ForeignKey(tbl_recruiter,on_delete=models.CASCADE)
class tbl_careerguidence(models.Model):
    careerguidence_details=models.CharField(max_length=50)
    careerguidence_photo=models.FileField(upload_to="Assets/Recruiterdocs/class/",null=True)
    careerguidence_date=models.DateField()
    careerguidence_time=models.TimeField()
    careerguidence_class=models.CharField(max_length=50)
    careerguidence_status=models.IntegerField(default=0)
    recruiter=models.ForeignKey(tbl_recruiter,on_delete=models.CASCADE)

    