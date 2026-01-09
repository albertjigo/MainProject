from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)
class tbl_adminreg(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_password=models.CharField(max_length=50)
class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)
    
class tbl_place(models.Model):
    place_name = models.CharField(max_length=50)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)
class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=50)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
class tbl_level(models.Model):
    level_name=models.CharField(max_length=50)
    level_duration=models.CharField(max_length=50)
class tbl_jobtype(models.Model):
    jobtype_name=models.CharField(max_length=50)
class tbl_jobcategory(models.Model):
    jobcategory_name=models.CharField(max_length=50)
class tbl_examtype(models.Model):
    examtype_name=models.CharField(max_length=50)
class tbl_exam(models.Model):
    exam_name=models.CharField(max_length=50)
    exam_mark=models.CharField(max_length=50)
    examtype=models.ForeignKey(tbl_examtype,on_delete=models.CASCADE)
    level=models.ForeignKey(tbl_level,on_delete=models.CASCADE)
class tbl_question(models.Model):
    question_question=models.CharField(max_length=50)
    question_file=models.FileField(upload_to="Assets/Admindocs/Questions/",null=True)
    exam=models.ForeignKey(tbl_exam,on_delete=models.CASCADE)
class tbl_option(models.Model):
    option_option=models.CharField(max_length=50)
    option_status=models.IntegerField(default=0)
    question=models.ForeignKey(tbl_question,on_delete=models.CASCADE)