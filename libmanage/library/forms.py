from django import forms

class registrationform(forms.Form):
    username = forms.CharField(max_length=37)
    email = forms.EmailField()
    passcode = forms.IntegerField()
    firstname = forms.CharField(max_length=37)
    lastname = forms.CharField(max_length=37)
    role = forms.CharField(max_length=7)
    phoneno = forms.IntegerField()