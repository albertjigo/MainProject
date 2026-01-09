from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# Create your views here.

def UserRegistration(request):
    district=tbl_district.objects.all()
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_number')
        address=request.POST.get('txt_address')
        password=request.POST.get('txt_pass')
        photo=request.FILES.get('file_photo')
        place=tbl_place.objects.get(id=request.POST.get('sel_place'))
        checkuser = tbl_userreg.objects.filter(user_email=email).count()
        if checkuser > 0:
            return render(request,"Guest/UserRegistration.html",{'msg':'EMAIL ALREADY EXIST'})
        else:
            tbl_userreg.objects.create(user_name=name,user_email=email,user_contact=contact,user_address=address,user_password=password,user_photo=photo,place=place)
            return render(request,'Guest/UserRegistration.html',{'msg':'User Registered'})
    else:
        return render(request,'Guest/UserRegistration.html',{'districtdata':district})

def ajaxplace(request):
    did = request.GET.get("did")
    place = tbl_place.objects.filter(district=did)
    return render(request,"Guest/AjaxPlace.html",{'placedata':place})


def  Login(request):
    if request.method=="POST":
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_pass')

        admincount= tbl_adminreg.objects.filter(admin_email=email,admin_password=password).count()
        usercount=tbl_userreg.objects.filter(user_email=email,user_password=password).count()
        recruitercount=tbl_recruiter.objects.filter(recruiter_email=email,recruiter_password=password).count()
       
        if admincount > 0:
            admindata= tbl_adminreg.objects.get(admin_email=email,admin_password=password)
            request.session['aid'] = admindata.id
            return redirect("Admin:Homepage")
        elif usercount > 0:
            userdata= tbl_userreg.objects.get(user_email=email,user_password=password)
            request.session['uid'] = userdata.id
            return redirect("User:Homepage")
        elif recruitercount > 0:
            recruiterdata= tbl_recruiter.objects.get(recruiter_email=email,recruiter_password=password)
            request.session['rid'] = recruiterdata.id
            return redirect("Recruiter:Homepage")
        return render(request,'Guest/Login.html',{'msg':"Invalid Email Or Password.."})
    else:
        return render(request,'Guest/Login.html')
def Recruiterregistration(request):
    district=tbl_district.objects.all()
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_password')
        address=request.POST.get('txt_address')
        photo=request.FILES.get('file_photo')
        proof=request.FILES.get('file_proof')
        licence=request.FILES.get('file_licence')
        contact=request.POST.get('txt_contact')
        place=tbl_place.objects.get(id=request.POST.get('sel_place'))
        checkrecruiter = tbl_recruiter.objects.filter(recruiter_email=email).count()
        if checkrecruiter > 0:
            return render(request,"Guest/Recriterregistration.html",{'msg':'EMAIL ALREADY EXIST'})
        else:
            tbl_recruiter.objects.create(recruiter_name=name,recruiter_email=email,recruiter_password=password,recruiter_address=address,recruiter_photo=photo,recruiter_proof=proof,recruiter_licence=licence,recruiter_contact=contact,place=place)
            return render(request,'Guest/Recruiterregistration.html',{'msg':'Recruiter Registered'})
    else:
        return render(request,'Guest/Recruiterregistration.html',{'districtdata':district})