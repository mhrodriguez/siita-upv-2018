from django import forms

class RegForm(forms.Form):
    nombres = forms.CharField(max_length=45)
    tipo = forms.CharField(max_length=15)
    fecha = forms.DateField()
    lugar = forms.CharField(max_length=45)
    comentarios = forms.CharField(widget=forms.Textarea)