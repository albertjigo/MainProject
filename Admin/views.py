from django.shortcuts import render,redirect
from Admin.models import*
from Guest.models import*
from User.models import*

# Create your views here.
def logout(request):
    del request.session['aid']
    return redirect("Guest:Login")
def Homepage(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        Admin = tbl_adminreg.objects.get(id=request.session['aid'])
        return render(request,"Admin/HomePage.html",{'Admin':Admin})

def Adminregistration(request):
    data=tbl_adminreg.objects.all()
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_password')
        checkadmin = tbl_adminreg.objects.filter(admin_email=email).count()
        if checkadmin > 0:
            return render(request,"Admin/Adminregistration.html",{'msg':'EMAIL ALREADY EXIST'})
        else:
            tbl_adminreg.objects.create(admin_name=name,admin_email=email,admin_password=password) 
            return render(request,'Admin/AdminRegistration.html',{'msg':'Data Inserted'})
    else:
        return render(request,'Admin/AdminRegistration.html',{"ad":data})
def District(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        data=tbl_district.objects.all()
    if request.method=="POST":
        district=request.POST.get('txt_district')
        tbl_district.objects.create(district_name=district)
        return render(request,'Admin/District.html',{'msg':'Data Inserted'})
    else:        
        return render(request,'Admin/District.html',{"dis":data})
def Category(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        data=tbl_category.objects.all()
    if request.method=="POST":
        category=request.POST.get('txt_category')
        checkcategory = tbl_category.objects.filter(category_name=category).count()
        if checkcategory > 0:
            return render(request,"Admin/Category.html",{'msg':'EMAIL ALREADY EXIST'})
        else:
            tbl_category.objects.create(category_name=category)
            return render(request,'Admin/Category.html',{'msg':'Data Inserted'})
    else:
        return render(request,'Admin/Category.html',{"cat":data})
def deldistrict(request,id):
    tbl_district.objects.get(id=id).delete()
    return redirect("Admin:District")
def delcategory(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return redirect("Admin:Category")
def editcategory(request,id):
    editdata=tbl_category.objects.get(id=id)
    if request.method=="POST":
        category=request.POST.get("txt_category")
        editdata.category_name=category
        editdata.save()
        return redirect("Admin:Category")
    else:
        return render(request,'Admin/Category.html',{'editdata':editdata})
def editdistrict(request,id):
    editdata=tbl_district.objects.get(id=id)
    if request.method=="POST":
        district=request.POST.get("txt_district")
        editdata.district_name=district
        editdata.save()
        return redirect("Admin:District")
    else:
        return render(request,"Admin/District.html",{'editdata':editdata})
def deladmin(request,id):
    tbl_adminreg.objects.get(id=id).delete()
    return redirect("Admin:Adminregistration")
def editadmin(request,id):
    editdata=tbl_adminreg.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get("txt_name")
        editdata.admin_name=name
        email=request.POST.get("txt_email")
        editdata.admin_email=email
        password=request.POST.get("txt_password")
        editdata.admin_password=password
        editdata.save()
        return redirect("Admin:Adminregistration")
    else:
        return render(request,'Admin/AdminRegistration.html',{'editdata':editdata})
def Place(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        place=tbl_place.objects.all()
        dist=tbl_district.objects.all()
    if request.method=="POST":
        district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        place=request.POST.get('txt_place')
        tbl_place.objects.create(place_name=place, district=district)
        return render(request,'Admin/Place.html',{'msg':'Data Inserted'})
    else:
        return render(request,"Admin/Place.html",{'districtdata':dist,'place':place})
def Subcategory(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        subcategory=tbl_subcategory.objects.all()
        cat=tbl_category.objects.all()
    if request.method=="POST":
        category=tbl_category.objects.get(id=request.POST.get('sel_category'))
        subcategory=request.POST.get("txt_sub")
        tbl_subcategory.objects.create(subcategory_name=subcategory, category=category)
        return render(request,"Admin/Subcategory.html",{'msg':'Data Inserted'})
    else:
        return render(request,"Admin/Subcategory.html",{'categorydata':cat,'subcategorydata':subcategory})
def delplace(request,id):
    tbl_place.objects.get(id=id).delete()
    return redirect("Admin:Place")
def editplace(request,id):
    district=tbl_district.objects.all()
    editdata=tbl_place.objects.get(id=id)
    if request.method=="POST":
        place=request.POST.get("txt_place")
        editdata.place_name=place
        district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        editdata.district=district
        editdata.save()
        return redirect("Admin:Place")
    else:
        return render(request,'Admin/Place.html',{'editdata':editdata,'districtdata':district})
def delsub(request,id):
    tbl_subcategory.objects.get(id=id).delete()
    return redirect("Admin:Subcategory")
def editsub(request,id):
    category=tbl_category.objects.all()
    editdata=tbl_subcategory.objects.get(id=id)
    if request.method=="POST":
        subcategory=request.POST.get('txt_sub')
        editdata.subcategory_name=subcategory
        category=tbl_category.objects.get(id=request.POST.get('sel_category'))
        editdata.category=category
        editdata.save()
        return redirect('Admin:Subcategory')
    else:
        return render(request,'Admin/Subcategory.html',{'editdata':editdata,'categorydata':category})
def Userlist(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        user=tbl_userreg.objects.all()
        return render(request,'Admin/Userlist.html',{'userdata':user})
def Recruiterverification(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        recruiter=tbl_recruiter.objects.all()
        return render(request,'Admin/Recruiterverification.html',{'recruiterdata':recruiter})
def acceptrecruiter(request,id):
    recruiter= tbl_recruiter.objects.get(id=id)
    recruiter.recruiter_status=1
    recruiter.save()
    return render(request,'Admin/Recruiterverification.html',{'msg':'Accepted'})
def rejectrecruiter(request,id):
    recruiter=tbl_recruiter.objects.get(id=id)
    recruiter.recruiter_status=2
    recruiter.save()
    return render(request,'Admin/Recruiterverification.html',{'msg':'Rejected'})  
def Level(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        leveldata=tbl_level.objects.all()
    if request.method=="POST":
        level=request.POST.get('txt_level')
        duration=request.POST.get('txt_duration')
        tbl_level.objects.create(level_name=level,level_duration=duration)
        return render(request,"Admin/Level.html",{'msg':'Data Inserted'})
    else:
        return render(request,"Admin/Level.html",{'level':leveldata})
def dellevel(request,id):
    tbl_level.objects.get(id=id).delete()
    return redirect("Admin:Level")
def editlevel(request,id):
    level=tbl_level.objects.all()
    editdata=tbl_level.objects.get(id=id)
    if request.method=="POST":
        level=request.POST.get('txt_level')
        editdata.level_name=level
        duration=request.POST.get('txt_duration')
        editdata.level_duration=duration
        editdata.save()
        return redirect("Admin:Level")
    else:
        return render(request,'Admin/Level.html',{'editdata':editdata})
def Jobtype(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        jobdata=tbl_jobtype.objects.all()
    if request.method=="POST":
        jobtype=request.POST.get('txt_job')
        tbl_jobtype.objects.create(jobtype_name=jobtype)
        return render(request,"Admin/Jobtype.html",{'msg':'Data Inserted'})
    else:
        return render(request,"Admin/Jobtype.html",{'jobtype':jobdata})
def deljt(request,id):
    tbl_jobtype.objects.get(id=id).delete()
    return redirect("Admin:Jobtype")
def editjt(request,id):
    jobtype=tbl_jobtype.objects.all()
    editdata=tbl_jobtype.objects.get(id=id)
    if request.method=="POST":
        jobtype=request.POST.get('txt_job')
        editdata.jobtype_name=jobtype
        editdata.save()
        return redirect("Admin:Jobtype")
    else:
        return render(request,'Admin/Jobtype.html',{'editdata':editdata})
def Jobcategory(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        jobcatdata=tbl_jobcategory.objects.all()
    if request.method=="POST":
        jobcategory=request.POST.get('txt_jobcat')
        tbl_jobcategory.objects.create(jobcategory_name=jobcategory)
        return render(request,"Admin/Jobcategory.html",{'msg':'Data Inserted'})
    else:
        return render(request,"Admin/Jobcategory.html",{'jobcategory':jobcatdata})
def deljc(request,id):
    tbl_jobcategory.objects.get(id=id).delete()
    return redirect("Admin:Jobcategory")
def editjc(request,id):
    jobcategory=tbl_jobcategory.objects.all()
    editdata=tbl_jobcategory.objects.get(id=id)
    if request.method=="POST":
        jobcategory=request.POST.get('txt_jobcat')
        editdata.jobcategory_name=jobcategory
        editdata.save()
        return redirect("Admin:Jobcategory")
    else:
        return render(request,'Admin/Jobcategory.html',{'editdata':editdata})
def Examtype(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        examtdata=tbl_examtype.objects.all()
    if request.method=="POST":
        examtype=request.POST.get('txt_examtype')
        tbl_examtype.objects.create(examtype_name=examtype)
        return render(request,"Admin/Examtype.html",{'msg':'Data Inserted'})
    else:
        return render(request,"Admin/Examtype.html",{'examtype':examtdata})
def delext(request,id):
    tbl_examtype.objects.get(id=id).delete()
    return redirect("Admin:Examtype")
def editext(request,id):
    examtype=tbl_examtype.objects.all()
    editdata=tbl_examtype.objects.get(id=id)
    if request.method=="POST":
        examtype=request.POST.get('txt_examtype')
        editdata.examtype_name=examtype
        editdata.save()
        return redirect("Admin:Examtype")
    else:
        return render(request,'Admin/Examtype.html',{'editdata':editdata})
def Notes(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        examtype=tbl_examtype.objects.all()
        notes=tbl_notes.objects.filter(user__isnull=True)
    if request.method=="POST":
        title=request.POST.get('txt_title')
        details=request.POST.get('txt_details')
        file=request.FILES.get('file_note')
        examtype=tbl_examtype.objects.get(id=request.POST.get('sel_et'))
        tbl_notes.objects.create(notes_title=title,notes_details=details,notes_file=file,examtype=examtype,notes_status=1)
        return render(request,'Admin/Notes.html',{'msg':"Inserted"})        
    else:
        return render(request,'Admin/Notes.html',{'examtype':examtype,'notes':notes})
def notedel(request,id):
    tbl_notes.objects.get(id=id).delete()
    return redirect("Admin:Notes")
def Viewnotes(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        userdata= tbl_userreg.objects.all()
        notes=tbl_notes.objects.filter(user__in=userdata)
        return render(request,'Admin/Viewnotes.html',{'notes':notes})
def acceptnotes(request,id):
    notes= tbl_notes.objects.get(id=id)
    notes.notes_status=1
    notes.save()
    return render(request,'Admin/Viewnotes.html',{'msg':'Verified'})
def rejectnotes(request,id):
    notes=tbl_notes.objects.get(id=id)
    notes.notes_status=2
    notes.save()
    return render(request,'Admin/Viewnotes.html',{'msg':'Rejected'})
def Examination(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        Examtype=tbl_examtype.objects.all()
        Level=tbl_level.objects.all()
        exam=tbl_exam.objects.all()
    if request.method=='POST':
        name=request.POST.get('txt_name')
        mark=request.POST.get('txt_mark')
        examtype=tbl_examtype.objects.get(id=request.POST.get('sel_exam'))
        level=tbl_level.objects.get(id=request.POST.get('sel_level'))
        tbl_exam.objects.create(exam_name=name,exam_mark=mark,examtype=examtype,level=level)
        return render(request,'Admin/Examination.html',{'msg':'Inserted'})
    else:
        return render(request,'Admin/Examination.html',{'Examtype':Examtype,'Level':Level,'exam':exam})
def dele(request,id):
    tbl_exam.objects.get(id=id).delete()
    return redirect("Admin:Examination")
def Question(request,id):
    exam=tbl_exam.objects.get(id=id)
    Question=tbl_question.objects.all()
    if request.method=="POST":
        question=request.POST.get('txt_question')
        file=request.FILES.get('file_q')
        tbl_question.objects.create(question_question=question,question_file=file,exam=exam)
        return render(request,'Admin/Question.html',{'msg':'Inserted','id':id})
    else:
        return render(request,'Admin/Question.html',{'Question':Question,'id':id})
def delq(request,qid,id):
    tbl_question.objects.get(id=qid).delete()
    return redirect("Admin:Question",id)
def Addoption(request,id):
    opt=tbl_option.objects.all()
    question=tbl_question.objects.get(id=id)
    if request.method=="POST":
        option=request.POST.get('txt_option')
        tf=request.POST.get('rd')
        tbl_option.objects.create(option_option=option,option_status=tf,question=question)
        return render(request,'Admin/Addoption.html')
    else:
        return render(request,'Admin/Addoption.html',{'opt':opt,'id':id})
def delo(request,did,id):
    tbl_option.objects.get(id=did).delete()
    return redirect("Admin:Addoption",id)
def Viewcomplaint(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:    
        comp=tbl_complaint.objects.filter(complaint_status=0)
        rcomp=tbl_complaint.objects.filter(complaint_status=1)
        return render(request,'Admin/Viewcomplaint.html',{'comp':comp,'rcomp':rcomp})
def Reply(request,id):
    complaint=tbl_complaint.objects.get(id=id)
    if request.method=="POST":
        reply=request.POST.get('txt_reply')
        complaint.complaint_reply=reply
        complaint.complaint_status=1
        complaint.save()
        return render(request,'Admin/Reply.html',{'msg':'Replied'})
    else:
        return render(request,'Admin/Reply.html')
def Notification(request):
    noti=tbl_notification.objects.all()
    if request.method=="POST":
        title=request.POST.get("txt_title")
        details=request.POST.get("txt_details")
        file=request.FILES.get("file")
        date=request.POST.get("date")
        tbl_notification.objects.create(notification_title=title,notification_details=details,notification_file=file,notification_todate=date)   
        return render(request,'Admin/Notification.html')
    else:
        return render(request,'Admin/Notification.html',{"noti":noti})
def deln(request,id):
    tbl_notification.objects.get(id=id).delete()
    return redirect("Admin:Notification")