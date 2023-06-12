from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post, Soport, Like, Comment, Payment

# Create your views here.

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            messages.error(request,'Las contraseñas no coinciden')
            return redirect('/register')
        User.objects.create_user(username, email=email, first_name=first_name, last_name=last_name, password=password)
        return redirect('/login')
    return render (request, 'register_page.html')
        
def login_page(request):
    if (request.method == 'POST'):
        username= request.POST.get('username')
        password= request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Se inició sesión correctamente')
                return redirect('/')
        messages.success(request, 'Datos incorrectos')
    return render(request,'login.html')

def home(request):
    return render(request, 'home.html')

def soport_page(request):
    if (request.method == 'POST'):
        email = request.POST.get('email')
        sugerencia = request.POST.get('sugerencia')
        Soport.objects.create(text = sugerencia, email = email)
        messages.success(request, 'Se envio la sugerencia')
    return render (request,'soport.html')

def logout_page(request):
    logout(request)
    return redirect ('/login/')

def publications(request):
    usuario = User.objects.get(username=request.user)
    posts= Post.objects.all().order_by('-created')

    if len(posts) == 0: posts = None
    data = {'usuario':usuario, 'posts': posts}   
    return render (request,'comment.html', data)

def posts(request):
    id = request.POST.get('id')
    text = request.POST.get('text')
    if(id is None and text !=''):
        Post.objects.create(text = text,user = request.user)
        messages.success(request, 'Post creado correctamente')
    return redirect('/comment/')

def like(request):
    usuario = User.objects.get(username=request.user)
    pId = request.POST.get('megusta')
    post = Post.objects.get(id=pId)
    try:
        comprobar = Like.objects.get(user= usuario, post= post)
        comprobar.delete()
        print("borrar")
    except:
        Like.objects.create(user = request.user,post = post)
        print("hola")
    return redirect('/comment/')

def comentar(request):
    p = Post.objects.get(id = request.POST.get('post'))
    Comment.objects.create(
        text = request.POST.get('text'),
        user = request.user,
        post = p
    )
    return redirect('/comment/')

def pay(request):
    if request.method == 'POST':
        bank = request.POST.get('bank')
        account_number = request.POST.get('account_number')
        page = request.POST.get('page')
        amount = request.POST.get('amount')
        user = request.user
        
        if bank == '' or account_number == '' or page == '' or amount == '':
            messages.error(request, 'Rellene todos los espacios')
            return redirect('/pay/')  # Redirige a la página 'pay.html'
        else:
            Payment.objects.create(bank=bank, account_number=account_number, page=page, user=user, amount=amount)
            messages.success(request, 'Solicitud de pago generada correctamente')
            return redirect('/')  # Redirige a la página 'pay.html'
    
    return render(request, 'pay.html')

def eliminar(request):
    usuario = User.objects.get(username=request.user)
    delete= Comment.objects.get(user=usuario)
    delete.delete()

    return redirect('/comment/')