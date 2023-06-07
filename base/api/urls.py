from django.urls import path
from . import views

urlpatterns = [
    path('', views.routes),
    path('usuarios/', views.usuarios),
    path('usuario/<int:id>', views.user),
    path('pagos/<int:id>', views.pagos),
    path('posts/<str:usuario>', views.posts),
]