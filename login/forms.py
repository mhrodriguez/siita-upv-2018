from django import forms

class LogForm(forms.Form):
    usuario = forms.CharField(max_length=10)
    contrasena = forms.CharField(max_length=20, widget=forms.PasswordInput)
