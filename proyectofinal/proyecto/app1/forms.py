from django import forms

class productosFormulario(forms.Form):
    nombre=forms.CharField()
    precio=forms.IntegerField()
    