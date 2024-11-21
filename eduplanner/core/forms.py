from django import forms

class testform(forms.Form):
    value = forms.CharField(max_length=64)

class loginform(forms.Form):
    email = forms.EmailField(max_length=128, widget=forms.TextInput(attrs={'id': "inputEmail", 'class': "form-control", 'aria-describedby': "emailHelp"}))
    password = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'id': "inputPassword", 'class': "form-control"}))

class registerform(forms.Form):
    name = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'id': "inputName", 'class': "form-control"}))
    email = forms.EmailField(max_length=128, widget=forms.TextInput(attrs={'id': "inputEmail", 'class': "form-control", 'aria-describedby': "emailHelp"}))
    password = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'id': "inputPassword", 'class': "form-control", 'oninput': "validatePassword()"}))
    pass_repeat = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'id': "inputRepeat", 'class': "form-control", 'oninput': "validatePassword()"}))
