from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from .models import Userdetails
# Create your views here.
def homepage(request):
    return render(request,'home.html')


def loginpage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('pass')
        print(uname,pass1)
        user=authenticate(request,username=uname,password=pass1)
        if user is not  None:
            login(request,user)
            messages.success(request,"Logged In")
            return redirect('home')
        else:
            messages.error(request,"Invalid Credential")
    return render(request,'login.html')


def signuppage(request):
    if request.method=='POST':
        uname=request.POST.get('name')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('re_password')
        if pass1 != pass2:
            messages.error(request,"Password Not Matched")
        print(uname,pass1)
        user_check = Userdetails.objects.filter(uemail=email).exists()
        if user_check:
            messages.error(request,"User already exists!!!")
            return redirect('/signup')
        my_user = User.objects.create_user(email,uname,pass1)
        my_user.save()
        messages.success(request,"Registered Successfully")
        return  redirect('login')
    return render(request,'signup.html')


def createpage(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        if request.method=='POST':
            uemail=request.POST.get('uemail')
            usname=request.POST.get('usname')
            desg=request.POST.get('desg')
            port=request.POST.get('port')
            res = request.POST.get('res')
            web = request.POST.get('web')
            linked = request.POST.get('linked')
            insta = request.POST.get('insta')
            fb = request.POST.get('fb')
            hack = request.POST.get('hack')
            codechef = request.POST.get('codechef')
            leet = request.POST.get('leet')
            gthub = request.POST.get('gthub')
            gfg = request.POST.get('gfg')
            name_check = Userdetails.objects.filter(uemail=uemail).exists()
            print(name_check)
            if name_check == True:
                rem = Userdetails.objects.filter(uemail=uemail)
                print(rem)
                rem.delete()
                newdet = Userdetails(uemail=uemail,usname=usname,desg=desg,port=port,res=res,web=web,linked=linked,insta=insta,fb=fb,hack=hack,codechef=codechef,leet=leet,gthub=gthub,gfg=gfg)
                newdet.save()
                messages.success(request,"Your Profile Successfully Created")
                return redirect('/priview')
            print(uemail)   
            details = Userdetails(uemail=uemail,usname=usname,desg=desg,port=port,res=res,web=web,linked=linked,insta=insta,fb=fb,hack=hack,codechef=codechef,leet=leet,gthub=gthub,gfg=gfg)
            details.save()
            messages.success(request,"Your Profile Successfully Created")
            return redirect('/priview')
        elif request.method=='GET':
            return render(request,'create.html')
        else:
            return HttpResponse("Error")

def editpage(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        if request.method=='POST':
            uemail=request.POST.get('uemail')
            usname=request.POST.get('usname')
            desg=request.POST.get('desg')
            port=request.POST.get('port')
            res = request.POST.get('res')
            web = request.POST.get('web')
            linked = request.POST.get('linked')
            insta = request.POST.get('insta')
            fb = request.POST.get('fb')
            hack = request.POST.get('hack')
            codechef = request.POST.get('codechef')
            leet = request.POST.get('leet')
            gthub = request.POST.get('gthub')
            gfg = request.POST.get('gfg')
            name_check = Userdetails.objects.filter(uemail=uemail).exists()
            print(name_check)
            if name_check == True:
                rem = Userdetails.objects.filter(uemail=uemail)
                rem.delete()
                newdet = Userdetails(uemail=uemail,usname=usname,desg=desg,port=port,res=res,web=web,linked=linked,insta=insta,fb=fb,hack=hack,codechef=codechef,leet=leet,gthub=gthub,gfg=gfg)
                newdet.save()
                messages.success(request,"Details Submitted")
                emps = Userdetails.objects.filter(uemail=uemail)
                context={
                    'emps':emps
                }
                return render(request,'priview.html',context)
            details = Userdetails(uemail=uemail,usname=usname,desg=desg,port=port,res=res,web=web,linked=linked,insta=insta,fb=fb,hack=hack,codechef=codechef,leet=leet,gthub=gthub,gfg=gfg)
            details.save()
            messages.success(request,"Details Submitted")
            emps = Userdetails.objects.filter(uemail=uemail)
            context={
                'emps':emps
            }
            return render(request,'priview.html',context)
        elif request.method=='GET':
            username = request.user.username
            emps = Userdetails.objects.filter(uemail=username)
            context={
                'emps':emps
            }
            return render(request,'edit.html',context)
        else:
            return HttpResponse("Error")


def priviewpage(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:  
        username = request.user.username
        emps = Userdetails.objects.all()
        print(username)
        if username:
            emps = emps.filter(uemail=username)
            context = {
                'emps':emps
            }
            return render(request,'priview.html',context)

def logoutpage(request):
    auth_logout(request)
    messages.success(request,"Logout Succesfully")
    return redirect('/')