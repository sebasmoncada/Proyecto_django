from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register_page),
    path('login/',views.login_page),
    path('',views.home),
    path('soport/', views.soport_page),
    path('logout/',views.logout_page),
    path('comment/',views.publications),
    path('publish/',views.posts),
    path('megusta/', views.like),
    path('comentario/', views.comentar),
    path('pay/',views.pay),
]