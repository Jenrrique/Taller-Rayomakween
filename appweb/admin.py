from django.contrib import admin
from .models import *
# Register your models here.

class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre']
    list_editable = ['nombre']
    search_fields = ['rut']

admin.site.register(Especialidad)
admin.site.register(Profesional, ProfesionalAdmin)
admin.site.register(Contacto)
admin.site.register(Postular)
admin.site.register(Solicitud)
admin.site.register(Trabajo)
