from django.shortcuts import render
from django.http import HttpResponse
from .models import cliente, reservacion
from django.views.generic import ListView, DetailView, CreateView


#aqui es donde estara el login
def arranca(request):
	return render(request, 'base/arranca.html')

def inicio(request):
	return render(request, 'base/inicio.html')

def ver_clientes(request):
	context = {
				'mira' : cliente.objects.all()	
	}
	return render(request, 'base/ver_clientes.html', context)

def agregar_cliente(request):
	return render(request, 'base/agregar_clientes.html', context)

def ver_reservaciones(request):
	context = {
				'mira' : reservacion.objects.all()	
	}
	return render(request, 'base/ver_reservaciones.html', context)

class ReservacionView(ListView):
	model = reservacion
	template_name = 'base/ver_reservaciones.html'
	context_object_name = 'mira'
	ordering = ['entregado','entrega']

class ReservacionDetailView(DetailView):
	model = reservacion
	template_name = 'base/ver_detail.html'
	context_object_name = 'mira'
	ordering = ['entregado','entrega']

class ReservacionCreateView(CreateView):
	model = reservacion
	fields = ['modelo', 'camisa','corbata','monio','costo','anticipo','saldo','deposito','entrega','devolucion','entregado',]
	template_name = 'base/agregar_reservacion_form.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class ClienteCreateView(CreateView):
	model = cliente
	fields = ['nombre','apellido','telefono','pecho','cintura','largo_pantalon','manga','cuello',]
	template_name = 'base/agregar_cliente_form.html'

	def form_valid(self, form):
		return super().form_valid(form)



def agregar_reservacion(request):
	return render(request, 'base/agregar_reservacion.html', context)
