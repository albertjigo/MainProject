from django.shortcuts import render

# Create your views here.
def Sum(request):
    if request.method=="POST":
        a=request.POST.get("txt_num1")
        b=request.POST.get("txt_num2")
        c=int(a)+int(b)
        return render(request,'Basics/Sum.html', {'Result':c})
    else:
        return render(request,"Basics/Sum.html")
def Calculator(request):
    if request.method=="POST":
        a=int(request.POST.get('txt_num1'))
        b=int(request.POST.get('txt_num2'))
        btn=request.POST.get('btn_submit')
        if btn=='+':
            c=a+b
        elif btn=='-':
            c=a-b
        elif btn=='*':
            c=a*b
        elif btn=='/':
            c=a/b
        return render(request,'Basics/Calculator.html', {'Result':c})
    else:
        return render(request,"Basics/Calculator.html") 
def Largest(request):
    if request.method=="POST":
        a=int(request.POST.get('txt_num1'))
        b=int(request.POST.get('txt_num2'))
        c=int(request.POST.get('txt_num3'))
        if a>c and a>b:
            d=a
        elif b>a and b>c:
            d=b
        elif c>a and c>b:
            d=c
        return render(request,'Basics/Largest.html',{'Result':d})
    else:
        return render(request,'Basics/Largest.html')