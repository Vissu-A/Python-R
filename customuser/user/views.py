from django.shortcuts import render
from user.forms import UserForm,ProfileForm,loginform
from django.contrib.auth.models import User
from user.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from django.http import HttpResponse,HttpResponseRedirect

@login_required
def logingview(request):
    # import pdb;pdb.set_trace()
    # if request.method == 'GET':
    #     form = loginform(request.GET)
    #     if form.is_valid():
    #         uname = form.cleaned_data['username']
    #         pword = form.cleaned_data['password']
    #         user = auth.authenticate(username=uname, password=pword)
    #
    #         if user is not None:
    #             auth.login(request, user)
    #             return HttpResponseRedirect('register/')
    #         else:
    #             return HttpResponse('invalid credentials!')
    # else:
    #     form = loginform()
    # return render(request,'welcome.html',{'form':form})
    #if request.user.is_authenticated():
        obj = User.objects.get(username=request.user.username)
        obj1 = Profile.objects.get(user=obj)
        return render(request,'welcome.html',{'obj':obj,'obj1':obj1})


def register(request):

    if request.method == 'POST':

        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            #uobj = User()
            fname = user_form.cleaned_data['first_name']
            lname = user_form.cleaned_data['last_name']
            email = user_form.cleaned_data['email']
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            #password = make_password(user_form.cleaned_data['password'])
            x = User.objects.create_user(username,email,password)
            x.first_name = fname
            x.last_name = lname
            x.save()
            # uobj.save(commit=False)
            # uobj.profile = Profile()
            # Profile.user_id = x.id
            # Profile.location = profile_form.cleaned_data['location']
            # Profile.save()
            #uobj.save()
            # user = User.objects.get(pk=user_id)
            # user.Profile.location = profile_form.cleaned_data['location']
            # user.save()
            pobj = Profile()
            #o = User.objects.get(username=uobj.username)
            pobj.user_id = x.id
            #pobj.user_id = o.id
            pobj.location = profile_form.cleaned_data['location']
            pobj.save()


    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'profile.html', {'user_form': user_form,'profile_form': profile_form})
