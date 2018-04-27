from django import forms

class RegForm(forms.Form):
    tipo = forms.CharField(max_length=15, required=True, widget=(forms.
    TextInput(attrs={"value":""})))
    fecha = forms.DateField(required=True, widget=forms.DateInput(attrs={"value"
    :""}))
    lugar = forms.CharField(max_length=45, required=True, widget=forms.TextInput
    (attrs={"value":""}))
    comentarios = forms.CharField(required=True, widget=forms.Textarea)