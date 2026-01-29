import random
from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from User.models import *
from Recruiter.models import*
from django.http import JsonResponse
import json
from django.db.models import Q
from datetime import datetime, timedelta , time, datetime

# Create your views here.
def logout(request):
    del request.session['uid']
    return redirect("Guest:index")
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
        jobdata=tbl_job.objects.filter(job_lastdate__gt=datetime.today())
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

def viewquestion(request, id):
    user = tbl_userreg.objects.get(id=request.session["uid"])
    exam = tbl_exam.objects.get(id=id)

    old_bodies = tbl_examinationbody.objects.filter(
        user=user,
        examination=exam
    )

    tbl_timmer.objects.filter(examinationbody__in=old_bodies).delete()

    exambody = tbl_examinationbody.objects.create(
        user=user,
        examination=exam,
        examinationbody_status=0
    )

    questions = tbl_question.objects.filter(exam=exam)

    optioncount = 0
    for q in questions:
        if tbl_option.objects.filter(question=q).exists():
            optioncount += 1

    return render(request, "User/ViewQuestion.html", {
        "questions": questions,
        "exambodyid": exambody.id,
        "optioncount": optioncount,
        "examination_id": exam.id
    })

def ajaxexamanswer(request):
    exam_answer = request.GET.get('answers')
    exambodyid = request.GET.get('exambodyid')
    answers_dict = json.loads(exam_answer)

    exambody = tbl_examinationbody.objects.get(id=exambodyid)

    for question_key, option_id in answers_dict.items():
        questionid = question_key.split("_")[1]
        correct_option = tbl_option.objects.get(
            question=questionid,
            option_status=1
        )

        tbl_examinationanswers.objects.create(
            examinationbody=exambody,
            question=tbl_question.objects.get(id=questionid),
            myanswer=tbl_option.objects.get(id=option_id) if option_id else None,
            correct_answer=correct_option
        )

    exambody.examinationbody_status = 1
    exambody.save()

    return JsonResponse({
        "msg": "Examination Submitted Successfully",
        "exambodyid": exambodyid
    })

def ajaxtimer(request):
    exambodyid = request.GET.get('exambodyid')
    exambody = tbl_examinationbody.objects.get(id=exambodyid)
    exam = exambody.examination

    timer_count = tbl_timmer.objects.filter(examinationbody=exambody).count()

    if timer_count > 0:
        timer = tbl_timmer.objects.get(examinationbody=exambody)

        if timer.timmer > 0:
            timer.timmer -= 1
            timer.save()

            minutes = timer.timmer // 60
            seconds = timer.timmer % 60

            return JsonResponse({
                "msg": f"{minutes:02d}:{seconds:02d}",
                "status": False
            })
        else:
            exambody.examinationbody_status = 1
            exambody.save()

            return JsonResponse({
                "msg": "Time's up",
                "status": True
            })

    else:
        total_seconds = exam.level.level_duration * 60

        tbl_timmer.objects.create(
            examinationbody=exambody,
            timmer=total_seconds
        )

        minutes = total_seconds // 60
        seconds = total_seconds % 60

        return JsonResponse({
            "msg": f"{minutes:02d}:{seconds:02d}",
            "status": False
        })



def successer(request):
    return render(request,"User/Success.html")

def viewresult(request, exambodyid):
    exambody = tbl_examinationbody.objects.get(
        id=exambodyid,
        user=request.session["uid"]
    )

    answers = tbl_examinationanswers.objects.filter(
        examinationbody=exambody
    )

    total_questions = answers.count()

    score = 0
    for a in answers:
        if a.myanswer and a.myanswer.id == a.correct_answer.id:
            score += 1

    if exambody.total_marks != score:
        exambody.total_marks = score
        exambody.save() 

    return render(request, "User/ViewResult.html", {
        "answers": answers,
        "score": score,                
        "total_questions": total_questions,
        "total": total_questions,       
    })


def my_exam_history(request):
    user = tbl_userreg.objects.get(id=request.session["uid"])

    attempts = (
        tbl_examinationbody.objects
        .filter(user=user, examinationbody_status=1)
        .select_related("examination", "examination__examtype", "examination__level")
        .order_by("-id")
    )

    return render(request, "User/MyExamHistory.html", {
        "attempts": attempts
    })



def chatpage(request,id):
    recruiter  = tbl_recruiter.objects.get(id=id)
    return render(request,"User/Chat.html",{"recruiter":recruiter})

def ajaxchat(request):
    from_user = tbl_userreg.objects.get(id=request.session["uid"])
    to_recruiter = tbl_recruiter.objects.get(id=request.POST.get("tid"))
    print(to_recruiter)
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,recruiter_to=to_recruiter,chat_file=request.FILES.get("file"))
    return render(request,"User/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_userreg.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(recruiter_from=tid) | Q(recruiter_to=tid))).order_by('chat_time')
    return render(request,"User/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(user_from=request.session["uid"]) & Q(recruiter_to=request.GET.get("tid")) | (Q(recruiter_from=request.GET.get("tid")) & Q(user_to=request.session["uid"]))).delete()
    return render(request,"User/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})
def Notification(request):
    noti=tbl_notification.objects.all()
    return render(request,"User/Notification.html",{"noti":noti})
def Feedback(request):
    feed=tbl_feedback.objects.filter(user=request.session["uid"])
    us = tbl_userreg.objects.get(id=request.session["uid"])
    if request.method=="POST":
        feedback=request.POST.get('txt_content')
        tbl_feedback.objects.create(feedback_content=feedback,user=us)
        return render(request,"User/Feedback.html",{'msg':'Feedback Added'})
    else:
        return render(request,"User/Feedback.html",{"feed":feed})

def fdel(request,id):
    tbl_feedback.objects.get(id=id).delete()
    return redirect("User:Feedback")
def Ajaxsearchjob(request):
    jc = request.GET.get("jc")
    jt = request.GET.get("jt")

    job = tbl_job.objects.filter(job_lastdate__gt=datetime.today())

    if jt:
        job = job.filter(jobtype_id=jt)

    if jc:
        job = job.filter(jobcategory_id=jc)

    return render(request, "User/Ajaxsearchjob.html", {'job': job})
