from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.conf import settings  # Importar settings para acceder a la variable
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import RegistroForm, LoginForm  # Importa el formulario personalizado
from .models import CustomUser

def home_view(request):
    # Si el usuario ya está autenticado, redirigirlo al dashboard
    if request.user.is_authenticated:
        return redirect('login:dashboard')
    
    # Si no está autenticado, mostrar la página de inicio
    return render(request, 'home.html')  # Plantilla en templates/home.html

def register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone_number = form.cleaned_data['phone_number']  # Campo adicional

            # Verificar duplicados si VERIFICAR_DUPLICADOS es True
            if settings.VERIFICAR_DUPLICADOS:
                # Verificar si el nombre de usuario ya existe
                if CustomUser.objects.filter(username=username).exists():
                    form.add_error('username', 'Este nombre de usuario ya está en uso.')
                    return render(request, 'login/register.html', {'form': form})

                # Verificar si el correo electrónico ya existe
                if CustomUser.objects.filter(email=email).exists():
                    form.add_error('email', 'Este correo electrónico ya está registrado.')
                    return render(request, 'login/register.html', {'form': form})

                # Verificar si el número de teléfono ya existe
                if CustomUser.objects.filter(phone_number=phone_number).exists():
                    form.add_error('phone_number', 'Este número de teléfono ya está en uso.')
                    return render(request, 'login/register.html', {'form': form})

            # Crear un nuevo usuario usando CustomUser
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                phone_number=phone_number  # Asegúrate de incluir el campo adicional
            )
            return redirect('login:login')  # Redirigir al login
    else:
        form = RegistroForm()  # Formulario vacío para GET

    return render(request, 'login/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)  # Autenticar al usuario
            if user is not None:
                login(request, user)  # Iniciar sesión
                return redirect('login:dashboard')  # Redirigir a la página deseada
            else:
                form.add_error(None, "Nombre de usuario o contraseña incorrectos.")  # Mensaje de error
    else:
        form = LoginForm()  # Formulario vacío para GET

    return render(request, 'login/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login:home')  # Redirige a la vista 'home'

@login_required  # Asegura que solo los usuarios autenticados puedan acceder
def dashboard_view(request):
    return render(request, 'dashboard.html')  # Renderiza la plantilla dashboard.html