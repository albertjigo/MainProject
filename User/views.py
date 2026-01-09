from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from User.models import *
from Recruiter.models import*

# Create your views here.
def Homepage(request):
    user = tbl_userreg.objects.get(id=request.session['uid'])
    return render(request,'User/Homepage.html',{'user':user})
def Myprofile(request):
    
    user=tbl_userreg.objects.get(id=request.session['uid'])
    return render(request,'User/Myprofile.html',{'user':user})
def Editprofile(request):
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
    jobdata=tbl_job.objects.all()
    jobcategory=tbl_jobcategory.objects.all()
    jobtype=tbl_jobtype.objects.all()
    return render(request,'User/Viewjob.html',{'job':jobdata,'jobtype':jobtype,'jobcat':jobcategory})
def Viewmore(request,id):
    jobdata=tbl_job.objects.get(id=id)
    return render(request,'User/Viewmore.html',{'job':jobdata})
def Notes(request):
    user=tbl_userreg.objects.get(id=request.session['uid'])
    examtype=tbl_examtype.objects.all()
    notes=tbl_notes.objects.filter(user(id=request.session['uid']))
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
    apply=tbl_apply.objects.filter(user=request.session['uid'])
    return render(request,'User/Myrequest.html',{'apply':apply})
def delf(request,id):
    tbl_apply.objects.get(id=id).delete()
    return redirect("User:Myrequest")
def Viewexamination(request):
    exam=tbl_exam.objects.all()
    return render(request,'User/Viewexamination.html',{'exam':exam})
def Viewquestion(request,id):
    question=tbl_question.objects.filter(exam=id)
    return render(request,'User/Viewquestion.html',{'question':question})