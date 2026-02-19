from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Recruiter.models import*
from User.models import*
from datetime import datetime,date
from django.db.models import Q,Max



# Create your views here.
def logout(request):
    del request.session['rid']
    return redirect("Guest:Login")

def Homepage(request):
    if "rid" not in request.session:
        return redirect("Guest:Login")
    else:
        recruiter = tbl_recruiter.objects.get(id=request.session['rid'])
        return render(request,'recruiter/Homepage.html',{'recruiter':recruiter})
def Myprofile(request):
    if "rid" not in request.session:
        return redirect("Guest:Login")
    else:
        recruiter=tbl_recruiter.objects.get(id=request.session['rid'])
        return render(request,'recruiter/Myprofile.html',{'recruiter':recruiter})
def Editprofile(request):
    if "rid" not in request.session:
        return redirect("Guest:Login")
    else:
        recruiter=tbl_recruiter.objects.get(id=request.session['rid'])
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        address=request.POST.get('txt_address')
        recruiter.recruiter_name=name
        recruiter.recruiter_email=email
        recruiter.recruiter_contact=contact
        recruiter.recruiter_address=address
        recruiter.save()
        return redirect('Recruiter:Myprofile')
    else:
        return render(request,'Recruiter/Editprofile.html',{'recruiter':recruiter})
def Changepassword(request):
    if "rid" not in request.session:
        return redirect("Guest:Login")
    else:
        recruiter=tbl_recruiter.objects.get(id=request.session['rid'])
        recruiterpass = recruiter.recruiter_password
    if request.method=="POST":
        old=request.POST.get('txt_oldpass')
        new=request.POST.get('txt_newpass') 
        confirm=request.POST.get('txt_cpass')
        if recruiterpass == old:
            if new == confirm :
                recruiter.recruiter_password = new
                recruiter.save()
                return redirect('Recruiter:Myprofile')
            else:
                return render(request,'Recruiter/Changepassword.html',{'msg':"Password Mismatch"})
        else:
            return render(request,'Recruiter/Changepassword.html',{'msg':"Password Incorrect.."})
    else:
        return render(request,'Recruiter/Changepassword.html')
def Job(request):
    if "rid" not in request.session:
        return redirect("Guest:Login")
    else:
        recruiter = tbl_recruiter.objects.get(id=request.session['rid'])
        jobtype=tbl_jobtype.objects.all()
        jobcategory=tbl_jobcategory.objects.all()
        jobdata=tbl_job.objects.filter(recruiter=request.session['rid'])
    if request.method=="POST":
        title=request.POST.get('txt_title')
        details=request.POST.get('txt_details')
        date=request.POST.get('todate')
        experience=request.POST.get('txt_exp')
        requirment=request.POST.get('txt_req')
        jobtype=tbl_jobtype.objects.get(id=request.POST.get('sel_jt'))
        jobcategory=tbl_jobcategory.objects.get(id=request.POST.get('sel_jc'))
        tbl_job.objects.create(job_title=title,job_details=details,job_lastdate=date,job_experience=experience,job_requirment=requirment,jobtype=jobtype,jobcategory=jobcategory,recruiter=recruiter)
        return render(request,'Recruiter/Job.html',{'msg':'Data inserted'})
    else:
        return render(request,'Recruiter/Job.html',{'jobtypedata':jobtype,'jobcatdata':jobcategory,'jobdata':jobdata})
def deljob(request,id):
    tbl_job.objects.get(id=id).delete()
    return redirect("Recruiter:Job")
def editjob(request,id):
    jobcategory=tbl_jobcategory.objects.all()
    jobtype=tbl_jobtype.objects.all()
    editdata=tbl_job.objects.get(id=id)
    if request.method=="POST":
        title=request.POST.get('txt_title')
        editdata.job_title=title
        details=request.POST.get('txt_details')
        editdata.job_details=details
        todate=request.POST.get('todate')
        editdata.job_lastdate=todate
        experience=request.POST.get('txt_exp')
        editdata.job_experience=experience
        requirment=request.POST.get('txt_req')
        editdata.job_requirment=requirment
        jobtype=tbl_jobtype.objects.get(id=request.POST.get('sel_jt'))
        editdata.jobtype=jobtype
        jobcategory=tbl_jobcategory.objects.get(id=request.POST.get('sel_jc'))
        editdata.jobcategory=jobcategory
        editdata.save()
        return redirect('Recruiter:Job')
    else:
        return render(request,'Recruiter/Job.html',{'editdata':editdata,'jobtypedata':jobtype,'jobcatdata':jobcategory})
def Viewrequest(request):
    if "rid" not in request.session:
        return redirect("Guest:Login")
    else:
        apply=tbl_apply.objects.filter(job__recruiter=request.session['rid'])
        return render(request,'Recruiter/Viewrequest.html',{'apply':apply})
def acceptu(request,id):
    apply= tbl_apply.objects.get(id=id)
    apply.apply_status=1
    apply.save()
    return render(request,'Recruiter/Viewrequest.html',{'msg':'Accepted'})
def rejectu(request,id):
    apply=tbl_apply.objects.get(id=id)
    apply.apply_status=2
    apply.save()
    return render(request,'Recruiter/Viewrequest.html',{'msg':'Rejected'})
def chatpage(request,id):
    user  = tbl_userreg.objects.get(id=id)
    return render(request,"Recruiter/Chat.html",{"user":user})

def ajaxchat(request):
    from_recruiter = tbl_recruiter.objects.get(id=request.session["rid"])
    to_user = tbl_userreg.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),recruiter_from=from_recruiter,user_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"Recruiter/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    recruiter = tbl_recruiter.objects.get(id=request.session["rid"])
    chat_data = tbl_chat.objects.filter((Q(recruiter_from=recruiter) | Q(recruiter_to=recruiter)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Recruiter/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(recruiter_from=request.session["rid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(recruiter_to=request.session["aid"]))).delete()
    return render(request,"Recruiter/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})
def Careerguidence(request):
    if "rid" not in request.session:
        return redirect("Guest:Login")
    else:
        career=tbl_careerguidence.objects.all()
        recruiter=tbl_recruiter.objects.get(id=request.session['rid'])
    if request.method=="POST":
        details=request.POST.get("details")
        photo=request.POST.get("photo")
        date=request.POST.get("date")
        time=request.POST.get("time")
        link=request.POST.get("link")
        tbl_careerguidence.objects.create(careerguidence_details=details,careerguidence_photo=photo,careerguidence_date=date,careerguidence_time=time,recruiter=recruiter)
        return render(request,"Recruiter/Careerguidence.html")
    else:
        return render(request,"Recruiter/Careerguidence.html",{"career":career})
def delclass(request,id):
    tbl_careerguidence.objects.get(id=id).delete()
    return redirect("Recruiter:Careerguidence")