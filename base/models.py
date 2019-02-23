from django.db import models
from django.utils import timezone

class cliente(models.Model):
	nombre = models.CharField(max_length=128)
	apellido = models.CharField(max_length=128)
	telefono = models.DecimalField(max_digits=20, decimal_places=0)
	pecho_tallas = ( ('34', '34'),
		('36', '36'),
		('38', '38'),
		('40', '40'),
		('42', '42'),
		('44', '44'),
		('46', '46'),
		('48', '48'),
		('50', '50'),)	
	cintura_tallas = ( ('28', '28'),
		('30', '30'),
		('32', '32'),
		('34', '34'),
		('36', '36'),
		('38', '38'),
		('40', '40'),
		('42', '42'),)
	largo_tallas = ( ('34', '34'),
		('35', '35'),
		('36', '36'),
		('37', '37'),
		('38', '38'),
		('39', '39'),
		('40', '40'),
		('41', '41'),
		('42', '42'),)
	manga_tallas = ( ('22', '22'),
		('23', '23'),
		('24', '24'),
		('25', '25'),
		('26', '26'),)
	cuello_tallas = ( ('14', '14'),
		('15', '15'),
		('16', '16'),
		('17', '17'),
		('18', '18'),)
	pecho = models.CharField(max_length = 2, choices = pecho_tallas)
	cintura = models.CharField(max_length = 2, choices = cintura_tallas)
	largo_pantalon = models.CharField(max_length = 2, choices = largo_tallas)
	manga = models.CharField(max_length = 2, choices = manga_tallas)
	cuello = models.CharField(max_length = 2, choices = cuello_tallas)

	def __str__(self):
		return self.nombre 

class reservacion(models.Model):
	modelo_tallas = ( ('Tuxedo', 'Tuxedo'),
			('Slim Fit', 'Slim fit'),
			('Clasico', 'Clasico'),)
	camisa_tallas = ( ('Negra', 'Negra'),
			('Blanca', 'Blanca'),)
	corbata_tallas = ( ('Azul', 'Azul'),
			('Verde', 'Verde'),
			('Rojo', 'Rojo'),)
	monio_tallas = ( ('Si', 'Si'),
			('No', 'No'),)
	monio = models.CharField(max_length = 2, choices = monio_tallas)
	camisa = models.CharField(max_length = 10, choices = camisa_tallas)
	corbata = models.CharField(max_length = 10, choices = corbata_tallas)
	modelo = models.CharField(max_length = 10, choices = modelo_tallas)

	costo = models.DecimalField(max_digits=20, decimal_places=4)
	anticipo = models.DecimalField(max_digits=20, decimal_places=4)
	saldo = models.DecimalField(max_digits=20, decimal_places=4)
	deposito = models.DecimalField(max_digits=20, decimal_places=4)
	registro = models.DateTimeField(auto_now_add = True)
	entrega = models.DateField()
	devolucion = models.DateField()
	clienteid = models.ForeignKey(cliente, on_delete=models.CASCADE)

	entregado_opciones = ( ('Si', 'Si'),
			('No', 'No'),)
	entregado = models.CharField(max_length = 2, choices = entregado_opciones, default = 'No')

	def __str__(self):
		return self.clienteid.nombre
	def __str__(self):
		return self.clienteid.apellido
	



#class login(models.Model):