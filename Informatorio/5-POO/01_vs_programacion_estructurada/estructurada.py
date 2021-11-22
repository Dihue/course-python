# Definimos unos cuantos clientes

clientes = [
    {'Nombre':'Hector','Apellidos':'Costas Guzman','DNI':'11223344A'},
    {'Nombre':'Juan','Apellidos':'Gonzales Marquez','DNI':'55667788A'}
]


# Creamos una funcion que muestra un cliente en una lista a partir del DNI

def mostrar_clientes(clientes,dni):
    for c in clientes:
        if (dni == c['DNI']):
            print('{} {}'.format(c['Nombre'],c['Apellidos']))
            return
    print('Cliente no encontrado')


# Creamos una funcion que borra un cliente en una lista a partir del DNI

def borrar_cliente(clientes,dni):
    for i,c in enumerate(clientes):
        if (dni == c['DNI']):
            del(clientes[i])
            print(str(c),'> BORRADO')
            return
    print('Cliente no entontrado')


# Observa muy bien como se utiliza el codigo estructurado

print('\n---- Listado de Clientes ----')
print(clientes)

print('\n|-> Mostrar clientes por DNI:')
mostrar_clientes(clientes,'11223344A')
mostrar_clientes(clientes,'55667788A')

print('\n|-> Borrar clientes por DNI:')
borrar_cliente(clientes,'11223344A')
borrar_cliente(clientes,'55667788A')

print('\n---- Listado de Clientes ----')
print(clientes)