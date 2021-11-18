class Almacen():

	def __init__(self):
		self.lista_bebidas = []


	def agegar_bebida(self,bebida):
		# control de beibada valida
		test = isinstance(bebida, AguaMineral) or isinstance(bebida, Gaseosa)


class Bebida():

	def __init__(self,id,ca_litros,marca,precio):
		self.id = id
		self.ca_litros = ca_litros
		self.marca = marca
		self.precio = precio

	def get_precio(self):
		return self.precio

	def ver_info(self):
		print(f"ID: {self.id}")
		print(f"Cantidad de litros: {self.ca_litros}")
		print(f"Marca: {self.marca}")
		print(f"Precio: $ {self.precio}")


class AguaMineral():
	
	def __init__(self,id,ca_litros,marca,precio,origen):
		super().__init__(id,ca_litros,marca,precio)
		self.origen = origen

	def ver_info(self):
		super().ver_info()
		print(f"Origen: {self.origen}")


class Gaseosa():
	
	def __init__(self,id,ca_litros,marca,precio,p_azucar,tiene_descuento):
		super().__init__(id,ca_litros,marca,precio)
		self.p_azucar = p_azucar
		self.tiene_descuento = tiene_descuento
		self.descuento = 0.1

	def get_precio(self):
		if self.tiene_descuento:
			return self.precio*(1-self.descuento)
		return self.precio