from django.db import models
from Guest.models import *
from Recruiter.models import *

# Create your models here.
class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=50)
    complaint_desc=models.CharField(max_length=50)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_status=models.IntegerField(default=0)
    complaint_reply=models.CharField(max_length=50,null=True)
    user=models.ForeignKey(tbl_userreg,on_delete=models.CASCADE)
class tbl_notes(models.Model):
    notes_date=models.DateField(auto_now_add=True)
    notes_title=models.CharField(max_length=50)
    notes_details=models.CharField(max_length=50)
    notes_status=models.IntegerField(default=0)
    notes_file=models.FileField(upload_to="Assets/Userdocs/File/")
    user=models.ForeignKey(tbl_userreg,on_delete=models.CASCADE,null=True)
    examtype=models.ForeignKey(tbl_examtype,on_delete=models.CASCADE)
class tbl_apply(models.Model):
    apply_date=models.DateField(auto_now_add=True)
    apply_status=models.IntegerField(default=0)
    apply_file=models.FileField(upload_to="Assets/Userdocs/File/")
    user=models.ForeignKey(tbl_userreg,on_delete=models.CASCADE,null=True)
    job=models.ForeignKey(tbl_job,on_delete=models.CASCADE)



class tbl_examinationbody(models.Model):
    examination = models.ForeignKey(tbl_exam, on_delete=models.CASCADE)
    user = models.ForeignKey(tbl_userreg, on_delete=models.CASCADE)
    total_marks = models.IntegerField(default=0)
    examinationbody_status = models.IntegerField(default=0)

class tbl_examinationanswers(models.Model):
    examinationbody = models.ForeignKey(tbl_examinationbody, on_delete=models.CASCADE)
    question = models.ForeignKey(tbl_question, on_delete=models.CASCADE)
    myanswer = models.ForeignKey(tbl_option, on_delete=models.CASCADE, related_name="myanswer", null=True)
    correct_answer = models.ForeignKey(tbl_option, on_delete=models.CASCADE,related_name="correct_answer")
    examinationanswers_statusq = models.IntegerField(default=0)

class tbl_timmer(models.Model):
    timmer = models.TimeField()
    exam = models.ForeignKey(tbl_exam, on_delete=models.CASCADE)
    timmer_status = models.IntegerField(default=0)