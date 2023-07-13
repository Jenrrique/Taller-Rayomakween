from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name="home"),
    path('', home, name="home"),
    path('profesionales/', profesionales, name="profesionales"),
    path('trabajos/', trabajos, name="trabajos"),
    path('contacto/', contacto, name="contacto"),
    path('postular/', postular, name="postular"),
    path('listar_postular/', listar_postular, name="listar_postular"),
    path('detalle_postular/<pk>/', detalle_postular, name="detalle_postular"),
    path('solicitud/', solicitud, name="solicitud"),
    path('mantenedor/agregar_profesional/', agregar_profesional, name="agregar_profesional"),
    path('mantenedor/editar_profesional/<rutbuscado>', editar_profesional, name="editar_profesional"),
    path('mantenedor/eliminar_profesional/<rutbuscado>', eliminar_profesional, name="eliminar_profesional"),
    path('login_usuario/', login_usuario, name="login_usuario"),
    path('registro/', registro, name="registro"),
    path('administrador/', administrador, name="administrador"),
    path('mantenedor/listar_solicitud/', listar_solicitud, name="listar_solicitud"),
    path('mantenedor/listar_profesional/', listar_profesional, name="listar_profesional"),
    path('detalle_profesional/<pk>/', detalle_profesional, name="detalle_profesional"),
    path('detalle_trabajo/<pk>/', detalle_trabajo, name="detalle_trabajo"),
    path('detalle_solicitud/<pk>/', detalle_solicitud, name="detalle_solicitud")
]
