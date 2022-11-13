from django.shortcuts import render
from library.forms import registrationform
from library.models import uregister
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

@login_required
def welcome(request):

    return render(request,'welcome.html')

def register(request):
    #import pdb;pdb.set_trace()
    if request.method == 'GET':
        form = registrationform(request.GET)
        if form.is_valid():

            o = User()

            o.uname= form.cleaned_data['username']
            o.passcode = make_password(form.cleaned_data['passcode'])
            o.role = form.cleaned_data['role']
            o.fname = form.cleaned_data['firstname']
            o.lname = form.cleaned_data['lastname']
            o.phoneno = form.cleaned_data['phoneno']
            o.email = form.cleaned_data['email']
            o.save()
            #user = User.objects.create_user(o.uname,  o.email, o.passcode)
            #user.save()



    else:
        form = registrationform()
    return render(request,'register.html',{'form':registrationform()})

import pdb;pdb.set_trace()
def loggingout(request):
    if request.user.is_active == 1:
        logout(request)

