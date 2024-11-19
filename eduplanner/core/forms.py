from django import forms

class testform(forms.Form):
    value = forms.CharField(max_length=64)

