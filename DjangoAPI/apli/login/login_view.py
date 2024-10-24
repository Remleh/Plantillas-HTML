from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages

# view para login
def login_view(request):
    template_name = "login.html"

    # verifica si ya esta autenticado
    if request.user.is_authenticated and request.user.is_active:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Incorrect username or password or user account is suspended')
    return render(request, template_name)

#pagina de resgistro
def registro_view(request):
    template_name = "register.html"

    if request.method== 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_validation = request.POST['password_validation']

        if password != password_validation:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, template_name)
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe')
            return render(request, template_name)
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo ya esta registrado')
            return render(request, template_name)
        
        user = User(
            username=username,
            email = email,
            password=make_password(password),
            is_active = 0
        )
        user.save()
        messages.success(request, 'Cuenta creada exitosamente')
    return render(request, template_name)

def olvide_view(request):
    template_name = "forgot.html"
    return render(request,template_name)

def detalles_view(request):
    template_name = "details.html"
    return render(request,template_name)

def video_view(request):
    template_name = "watching.html"
    return render(request,template_name)

def blog_view(request):
    template_name = "blog.html"
    return render(request,template_name)

def blog_details_view(request):
    template_name = "blog-details.html"
    return render(request,template_name)

def logout_view(request):
    logout(request)
    return redirect('login')