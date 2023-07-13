from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactoForm, ProfesionalForm, SolicitudForm, PostularForm
from .models import Profesional, Solicitud, Trabajo, Postular

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def home(request):

    messages.success(request, " Este mensaje es de prueba")

    return render(request, "index.html")

def profesionales(request):
    profesionales = Profesional.objects.all()
    data = {
        'profesionales' : profesionales
    }

    if request.method == "POST":

        valor_buscado = request.POST.get("valor_buscado")    
        if valor_buscado != "":
            profesionales = Profesional.objects.filter(rut = valor_buscado)
            data["profesionales"] = profesionales
        else:
            data["profesionales"] = Profesional.objects.all()     

    return render(request, "profesionales.html", data)

def trabajos(request):
    trabajos = Trabajo.objects.all()
    data = {
        'trabajos' : trabajos
    }

    if request.method == "POST":

        valor_buscado = request.POST.get("valor_buscado")    
        if valor_buscado != "":
            trabajos = Trabajo.objects.filter(rut = valor_buscado)
            data["trabajos"] = trabajos
        else:
            data["trabajos"] = Trabajo.objects.all()     

    return render(request, "trabajos.html", data)


def contacto(request):

    data = {
        "form_contacto": ContactoForm,
        "mensaje": ""
    }

    if request.method == "POST":
        formulario = ContactoForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto creado."
        else:
            data["mensaje"] = "Error al crear el contacto."
            data["form_contacto"] = formulario  

    return render(request, "contacto.html", data)

def postular(request):

    data = {
        "form_postular": PostularForm,
        "mensaje": ""
    }

    if request.method == "POST":
        formulario = PostularForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Curriculum creado."
        else:
            data["mensaje"] = "Error al crear el Curriculum."
            data["form_postular"] = formulario  

    return render(request, "postular.html", data)

def solicitud(request):

    data = {
        "form_solicitud": SolicitudForm,
        "mensaje": ""
    }

    if request.method == "POST":
        formulario = SolicitudForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Solicitud creada."
        else:
            data["mensaje"] = "Error al crear la solicitud."
            data["form_solicitud"] = formulario  

    return render(request, "solicitud.html", data)

@login_required(login_url="/accounts/login")
@permission_required(['appweb.add_profesional'], login_url="/acounts/login/")
def agregar_profesional(request):

    data = {
        'form': ProfesionalForm
    }

    if request.method == 'POST':
        formulario = ProfesionalForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Profesional creado"
            return redirect(to="profesionales")
        else:
            data["mensaje"] = "No se ha creado el Profesional"
            data["form"] = formulario

    return render(request, "mantenedor/profesional/agregar.html", data)

def listar_profesional(request):

    profesionales = Profesional.objects.all()
    data = {
        'mis_profesionales' : profesionales
    }
    return render(request, "mantenedor/profesional/listar.html", data)

@login_required(login_url="/accounts/login")
def editar_profesional(request, rutbuscado):

    profesional = get_object_or_404(Profesional, rut=rutbuscado)
    data = {
        'form': ProfesionalForm(instance=profesional)
    }

    if request.method == "POST":
        formulario = ProfesionalForm(data=request.POST, instance=profesional, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_profesional")
        else:
            data["mensaje"] = "No se pudo editar el Profesional"
            data["form"] = formulario

    return render(request, "mantenedor/profesional/editar.html", data)

@login_required(login_url="/accounts/login")
def eliminar_profesional(request, rutbuscado):

    profesional = get_object_or_404(Profesional, rut=rutbuscado)

    profesional.delete()

    return redirect(to="listar_profesional")

def login_usuario(request):
    
    print("Bienvenido "+ request.user.username)

    if request.user.groups.filter(name='profesional'):
        print("es un profesional")

    return redirect(to='home')

def registro(request):

    data = {
        "mensaje": ""
    }

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        correo = request.POST.get("correo")
        password = request.POST.get("password")

        usu = User()
        usu.set_password(password)
        usu.username = nombre
        usu.email = correo
        usu.first_name = nombre
        usu.last_name = apellido

        grupoProf = Group.objects.get(name="profesional")

        try:
            usu.save()
            usu.groups.add(grupoProf)

            user = authenticate(username = usu.username, password = password)
            login(request, user)
            return redirect(to="home")
        except:
            data["mensaje"] = "Error al crear el usuario"    
    
    return render(request, "registration/registro.html")

def listar_solicitud(request):

    solicitudes = Solicitud.objects.all()
    data = {
        'mis_solicitudes' : solicitudes
    }
    return render(request, "mantenedor/solicitud/lista_solicitudes.html", data)

def listar_postular(request):

    postular = Postular.objects.all()
    data = {
        'mis_postular' : postular
    }
    return render(request, "listar_postular.html", data)

def administrador(request):

    messages.success(request, " Bienvenido")

    return render(request, "administrador.html")

def detalle_profesional(request, pk):
    profesional = get_object_or_404(Profesional, pk=pk)

    data = {
        "p": profesional
    }

    return render(request, "detalle_profesional.html", data)

def detalle_postular(request, pk):
    postular = get_object_or_404(Postular, pk=pk)

    data = {
        "c": postular
    }

    return render(request, "detalle_postular.html", data)

def detalle_trabajo(request, pk):
    trabajo = get_object_or_404(Trabajo, pk=pk)

    data = {
        "t": trabajo
    }

    return render(request, "detalle_trabajo.html", data)

def detalle_solicitud(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)

    data = {
        "s": solicitud
    }

    return render(request, "detalle_solicitud.html", data)




