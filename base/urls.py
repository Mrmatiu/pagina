from django.urls import path
from . import views
from .views import (ReservacionView, ReservacionDetailView, ReservacionCreateView, ClienteCreateView)


#app_name = 'base'

urlpatterns = [
    path('', views.arranca, name= 'arranca'),
    path('inicio/', views.inicio, name= 'inicio'),
    path('ver_clientes/', views.ver_clientes, name= 'ver_clientes'),
    path('ver_reservaciones/', ReservacionView.as_view(), name= 'ver_reservaciones'),

    path('ver/<int:pk>/', ReservacionDetailView.as_view(), name= 'ver_detail'),
    path('agregar_reservacion/new/', ReservacionCreateView.as_view(), name= 'agregar_reservacion'),
    path('agregar_cliente/new/', ClienteCreateView.as_view(), name= 'agregar_cliente'),



]
