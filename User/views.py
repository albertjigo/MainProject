import random
from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from User.models import *
from Recruiter.models import*
from django.http import JsonResponse
import json
from datetime import time, datetime, timedelta

# Create your views here.
def logout(request):
    del request.session['uid']
    return redirect("Guest:Login")
def Homepage(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        user = tbl_userreg.objects.get(id=request.session['uid'])
        return render(request,'User/Homepage.html',{'user':user})
def Myprofile(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        user=tbl_userreg.objects.get(id=request.session['uid'])
        return render(request,'User/Myprofile.html',{'user':user})
def Editprofile(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        user=tbl_userreg.objects.get(id=request.session['uid'])
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        address=request.POST.get('txt_address')
        user.user_name=name
        user.user_email=email
        user.user_contact=contact
        user.user_address=address
        user.save()
        return redirect('User:Myprofile')
    else:
        return render(request,'User/Editprofile.html',{'user':user})
def Changepassword(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        user=tbl_userreg.objects.get(id=request.session['uid'])
        userpassword = user.user_password
    if request.method=="POST":
        old=request.POST.get('txt_oldpass')
        new=request.POST.get('txt_newpass')
        confirm=request.POST.get('txt_cpass')
        if userpassword == old:
            if new == confirm :
                user.user_password = new
                user.save()
                return redirect('User:Myprofile')
            else:
                return render(request,'User/Changepassword.html',{'msg':"Password Mismatch"})
        else:
            return render(request,'User/Changepassword.html',{'msg':"Password Incorrect.."})
    else:
        return render(request,'User/Changepassword.html')
def Complaint(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        user=tbl_userreg.objects.get(id=request.session['uid'])
        Complaint=tbl_complaint.objects.filter(user=user)
    if request.method=="POST":
        title=request.POST.get('txt_title')
        desc=request.POST.get('txt_desc')
        tbl_complaint.objects.create(complaint_title=title,complaint_desc=desc,user=user)
        return render(request,'User/Complaint.html')        
    else:
        return render(request,'User/Complaint.html',{'Complaint':Complaint})
def Viewjob(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        jobdata=tbl_job.objects.all()
        jobcategory=tbl_jobcategory.objects.all()
        jobtype=tbl_jobtype.objects.all()
        return render(request,'User/Viewjob.html',{'job':jobdata,'jobtype':jobtype,'jobcat':jobcategory})
def Viewmore(request,id):
    jobdata=tbl_job.objects.get(id=id)
    return render(request,'User/Viewmore.html',{'job':jobdata})
def Notes(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        user=tbl_userreg.objects.get(id=request.session['uid'])
        examtype=tbl_examtype.objects.all()
        notes=tbl_notes.objects.filter(user_id=request.session['uid'])
    if request.method=="POST":
        title=request.POST.get('txt_title')
        details=request.POST.get('txt_details')
        file=request.FILES.get('file_note')
        examtype=tbl_examtype.objects.get(id=request.POST.get('sel_et'))
        tbl_notes.objects.create(notes_title=title,notes_details=details,notes_file=file,user=user,examtype=examtype)
        return render(request,'User/Notes.html',{'msg':"Inserted"})        
    else:
        return render(request,'User/Notes.html',{'examtype':examtype,'notes':notes})
def notedel(request,id):
    tbl_notes.objects.get(id=id).delete()
    return redirect("User:Notes")
def Viewnotes(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        notes=tbl_notes.objects.filter(notes_status=1)
        return render(request,'User/Viewnotes.html',{'notes':notes})
def Upload(request,id):
    user=tbl_userreg.objects.get(id=request.session['uid'])
    job=tbl_job.objects.get(id=id)
    if request.method=="POST":
        file=request.FILES.get('file_apply')
        tbl_apply.objects.create(apply_file=file,user=user,job=job)
        return render(request,'User/Upload.html',{'msg':'Applied'})
    else:
        return render(request,'User/Upload.html')
def Myrequest(request): 
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        apply=tbl_apply.objects.filter(user=request.session['uid'])
        return render(request,'User/Myrequest.html',{'apply':apply})
def delf(request,id):
    tbl_apply.objects.get(id=id).delete()
    return redirect("User:Myrequest")
# def Viewexamination(request):
#     if "uid" not in request.session:
#         return redirect("Guest:Login")
#     else:
#         exam = tbl_exam.objects.all()
#         examtypes = tbl_examtype.objects.all()
#     if request.method == "POST":
#         examtype_id = request.POST.get('examtype')
#         if examtype_id:
#             exam = exam.filter(examtype_id=examtype_id)
#     return render(request, 'User/Viewexamination.html', {'exam': exam,'examtypes': examtypes})

# def Viewquestion(request, id):
#     questions = tbl_question.objects.filter(exam_id=id)
    
#     question_data = []
#     for q in questions:
#         options = list(q.tbl_option_set.all())
#         random.shuffle(options)              
#         options = options[:4]               

#         question_data.append({'question': q,'options': options})

#     return render(request, 'User/Viewquestion.html', {'question_data': question_data})


def viewexam(request):
    exam = tbl_exam.objects.all()
    for i in exam:
        exambodycount = tbl_examinationbody.objects.filter(examination=i.id,user=request.session["uid"],examinationbody_status=1).count()
        if exambodycount > 0:
            i.examstatus = 1
    return render(request,"User/ViewExam.html",{'exam':exam})

def viewquestion(request,id):
    question = tbl_question.objects.filter(exam=id)
    optioncount = 0
    for i in question:
        count = tbl_option.objects.filter(question=i.id).count()
        if count > 0:
            optioncount = optioncount + 1
    examcount = tbl_examinationbody.objects.filter(examination=id,user=request.session["uid"]).count()
    if examcount > 0:
        exambodyid = tbl_examinationbody.objects.get(examination=id,user=request.session["uid"])
        return render(request,"User/ViewQuestion.html",{'questions':question,"exambodyid":exambodyid.id,"optioncount":optioncount,"examination_id":id})
    else:
        exambodyid = tbl_examinationbody.objects.create(user=tbl_userreg.objects.get(id=request.session["uid"]),examination=tbl_exam.objects.get(id=id))
        return render(request,"User/ViewQuestion.html",{'questions':question,"exambodyid":exambodyid.id,"optioncount":optioncount,"examination_id":id})

def ajaxexamanswer(request):
    exam_answer = request.GET.get('answers')
    answers_dict = json.loads(exam_answer)
    for question_key, option_id in answers_dict.items():
        questionid = question_key.split("_")[1]
        options = tbl_option.objects.get(question=questionid,option_status=1)
        if option_id == None:
            tbl_examinationanswers.objects.create(examinationbody=tbl_examinationbody.objects.get(id=request.GET.get('exambodyid')),question=tbl_question.objects.get(id=questionid),correct_answer=tbl_option.objects.get(id=options.id))
        else:
            tbl_examinationanswers.objects.create(examinationbody=tbl_examinationbody.objects.get(id=request.GET.get('exambodyid')),question=tbl_question.objects.get(id=questionid),myanswer=tbl_option.objects.get(id=option_id),correct_answer=tbl_option.objects.get(id=options.id))
    exambody = tbl_examinationbody.objects.get(id=request.GET.get('exambodyid'))
    exambody.examinationbody_status = 1
    exambody.save()
    return JsonResponse({"msg":"Examination Submitted Sucessfully..."})

def ajaxtimer(request):
    exam = tbl_exam.objects.get(id=request.GET.get('exam'))

    timecount = tbl_timmer.objects.filter(exam=exam).count()

    if timecount > 0:
        timer_obj = tbl_timmer.objects.get(exam=exam)

        if timer_obj.timmer > time(0, 0, 0):
            current_datetime = datetime.combine(datetime.today(), timer_obj.timmer)
            new_datetime = current_datetime - timedelta(seconds=1)
            new_time = new_datetime.time()

            timer_obj.timmer = new_time
            timer_obj.save()

            time_str = new_time.strftime("%H:%M:%S")
            return JsonResponse({"msg": time_str, "status": False})
        else:
            exam.examination_status = 2
            exam.save()
            return JsonResponse({"msg": "Time's up", "status": True})
    else:
        minutes = exam.level.level_duration  # minutes (int)
        hours = minutes // 60
        mins = minutes % 60

        start_time = time(hours, mins, 0)
        tbl_timmer.objects.create(exam=exam, timmer=start_time)

        return JsonResponse({"msg": ""})

def successer(request):
    return render(request,"User/Success.html")
