# Creo una estructura para los clientes

class Clientes:

    def __init__(self,dni,nombre,apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


# Creo una estructura para las empresas

class Empresa:

    def __init__(self,clientes=[]):
        self.clientes = clientes

    def mostrar_clientes(self,dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print('Cliente no encontrado')

    def borrar_cliente(self,dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del (self.clientes[i])
                print(str(c),">Borrado")
                return
        print('Cliente no entontrado')


# Ahora utilizaremos ambas estructuras

# Creamos un par de clientes
hector = Clientes('123123123A','Hector','Toledo')
denis = Clientes('321321321B','Denis','Nuñez')

# Creamos una empresa con los clientes inciales
empresa = Empresa(clientes=[hector,denis])

# Se muestran los clientes
print('\n|--> Lista de Clientes:')
print(empresa.clientes)

# Se muestran clientes por DNI
print('\n|--> Mostrar Clientes por DNI:')
# Se consulta clientes por DNI
empresa.mostrar_clientes('123123123A')
empresa.mostrar_clientes('321321321B')

print('\n|--> Borrar Clientes por DNI:')
# Se borra clientes por DNI
empresa.borrar_cliente('123123123A')
empresa.borrar_cliente('321321321B')

# Se muestran de nuevo los clientes
print('\n|--> Lista de Clientes:')
print(empresa.clientes)