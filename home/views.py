from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User,auth

from django.contrib import messages
from django.template import RequestContext
from home.models import Register
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'base.html')

def about(request):
    return render(request,'about.html')
def search(request):
    if request.method=='POST':
        srch=request.POST['srh']
        if srch:
            match=Register.objects.filter(Q(Donor_name__iexact=srch) | Q(Username__iexact=srch))

            if match:
                return render(request,'search.html',{'sr':match})
            else:
                messages.error(request,'No result found !!!')

        else:
            return HttpResponseRedirect('search')            
            
    return render(request,'search.html')    

def login(request):
    if request.method== 'POST':
        
        Username=request.POST['Username']
        Password=request.POST['Password']
        user=auth.authenticate(Username=Username,Password=Password)

        if User is not None:
            auth.login(request, User)
            return redirect("/")
        else:
            messages.info(request,"Invalid username or password")
            return redirect("login")
        '''
        else:
            messages.info(request,"Invalid username or password")
            return redirect("login")'''
    else:
        return render(request,'login.html')
def register(request):
    if request.method == "POST":
        Donor_name=request.POST['Donor_name']
        Contact_no=request.POST['Contact_no']
        Username=request.POST['Username']
        Password=request.POST['Password']
        Confirm_Password=request.POST['Confirm_Password']
        Blood_group=request.POST['Blood_group']
        blood_amt=request.POST['blood_amt']
        Rh_factor=request.POST['Rh_factor']
        Address=request.POST['Address']

        reg=Register(Donor_name=Donor_name,Contact_no=Contact_no,Username=Username,blood_amt=blood_amt,Password=Password,Blood_group=Blood_group,Rh_factor=Rh_factor,Address=Address)
        reg.save()
        print("register")
        return redirect('/')

    else:
        return render(request,'register.html',)    


def blood(request):   
    if request.method=='POST':
        srch=request.POST['b_group']
        srch1=request.POST['rh']

        if srch or srch1:
            match=Register.objects.filter(Q(Blood_group__iexact=srch) | Q(Rh_factor__iexact=srch1))
       

            if match:
                return render(request,'blood.html',{'sr':match})
            else:
                messages.error(request,'No result found !!!')

        else:
            return HttpResponseRedirect('blood')            
            
    return render(request,'blood.html')         

def store(request):
    r=Register.objects.all()
    return render(request,"store.html",{'r':r})    