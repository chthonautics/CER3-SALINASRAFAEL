from django import forms
from api.events import *

class testform(forms.Form):
    value = forms.CharField(max_length=64)

class loginform(forms.Form):
    email       = forms.EmailField(max_length=128, widget=forms.TextInput(attrs={'id': "inputEmail", 'class': "form-control", 'aria-describedby': "emailHelp"}))
    password    = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'id': "inputPassword", 'class': "form-control"}))

class registerform(forms.Form):
    name        = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'id': "inputName", 'class': "form-control"}))
    email       = forms.EmailField(max_length=128, widget=forms.TextInput(attrs={'id': "inputEmail", 'class': "form-control", 'aria-describedby': "emailHelp"}))
    password    = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'id': "inputPassword", 'class': "form-control", 'oninput': "validatePassword()"}))
    pass_repeat = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'id': "inputRepeat", 'class': "form-control", 'oninput': "validatePassword()"}))

class eventform(forms.Form):
    name            = forms.CharField(max_length=256, widget=forms.TextInput(attrs={'id': "inputName", 'class': "form-control"}))
    description     = forms.CharField(max_length=2048, widget=forms.Textarea(attrs={'id': "inputComment", 'class': "form-control"}))
    date_start      = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'id': "inputDateStart", 'class': "form-control", 'oninput': "verify()"}))
    date_end        = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'id': "inputDateEnd", 'class': "form-control", 'oninput': "verify()"}))
    forced          = forms.BooleanField(required=False)#widget=forms.BooleanField(attrs={'id': "inputForced", 'class': "form-control"}))
    event_type      = forms.ChoiceField(choices=eventTypes)#, widget=forms.ChoiceField(attrs={'id': "inputEventType", 'class': "form-control"}))