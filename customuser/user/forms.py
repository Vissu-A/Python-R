from django import forms
from django.contrib.auth.models import User
from user.models import Profile



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('location',)


class loginform(forms.Form):
    username = forms.CharField(max_length=27)
    password = forms.CharField(max_length=27)