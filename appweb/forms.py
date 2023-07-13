from django import forms
from .models import Contacto, Profesional, Solicitud, Postular

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = "__all__"

class PostularForm(forms.ModelForm):
    class Meta:
        model = Postular
        fields = "__all__"

class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = "__all__"

        widgets = {
            "fecha_nacimiento": forms.DateInput(attrs={'type': 'date'}, format=('%Y-%m-%d'))
        }

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = "__all__" 

        widgets = {
            "fecha": forms.DateInput(attrs={'type': 'date'}, format=('%Y-%m-%d'))
        }              