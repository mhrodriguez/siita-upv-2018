from django import forms

class in_mat(forms.Form):
    
    Matricula = forms.CharField(max_length=45, required=True, widget=forms.TextInput
    (attrs={"value":""}))
