from django.http import JsonResponse
from ..models import Post, Comment, Like, Payment
from django.contrib.auth.models import User

def routes(request):
    routes = [
        'GET /api/usuarios',
        'GET /api/usuario/id',
        'GET /api/posts/usuario',
        'GET /api/pagos/id',
    ]
    return JsonResponse(routes, safe=False)

def usuarios(request):
    usuarios= User.objects.all()
    data = []
    for usuario in usuarios:
        data.append({
            'username': usuario.username,
            'first_name': usuario.first_name,
            'last_name' : usuario.last_name,
            'email': usuario.email
        })

    return JsonResponse(data, safe=False)
    
def user(request,id):
    user = User.objects.get(id=id)
    user_dict = {
        'username': user.username,
            'first_name': user.first_name,
            'last_name' : user.last_name,
            'email': user.email
    }
    return JsonResponse(user_dict, safe=False)

def posts(request, usuario):
    data=[]
    id = User.objects.get(username=usuario)
    posts = Post.objects.filter(user=id)
    for post in posts:
        comentariosData = []
        comentarios = Comment.objects.filter(post=post)
        for comentario in comentarios:
            comentariosData.append({
                'username': comentario.user.username,
                'text': comentario.text
            })
        megustasData =[]
        megustas = Like.objects.filter(post=post)
        for megusta in megustas:
            megustasData.append({
                'username': megusta.user.username,
            })
        data.append({
            'username' : id.username,
            'text': post.text,
            'comentarios': comentariosData,
            'megustas': megustasData
        })
    return JsonResponse(data, safe=False)

def pagos(request,id):
    pagos = Payment.objects.get(id=id)
    pagos_dict= {
        'username': pagos.user.username,
        'banco': pagos.bank,
        'numero' : pagos.account_number,
        'montoTotal': pagos.amount
    }
    return JsonResponse(pagos_dict, safe=False)