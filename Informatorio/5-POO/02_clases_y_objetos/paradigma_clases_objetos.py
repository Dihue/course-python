# PARADIGMA DE PROGRAMACION ORIENTADA A OBJETOS
'''
Un PARADIGMA es el resultado de un proceso social en el cual un grupo de personas
desarrolla nuevas ideas y crea principios y practicas alrededor de esas ideas.

En programacion, se trata de un enfoque concreto de desarrollar y estructurar el
desarrollo de programas en base a Objetos.
'''

# CLASE
'''
Una CLASE es un metodo que define las propiedades y comportamientos de un tipo de
objeto concreto, en la instanciacion se hace la lectura de esas definiciones y se
crea un objeto a partir de ellas. Las clases son abstracciones que representan a 
un conjunto de objetos con sus comportamientos e interfaz comun.

Una clase se compone de dos partes:
    > Atributos: esto es, los datos que se refieren al estado del objeto.
    > Metodos: son funciones que pueden apliclarse a los objetos.
'''

# OBJETO
'''
Entidad provista de un conjuntos de propiedades o atributos(datos) y de comporta-
mientos o funcionalidad(metodos), los mismos que consecuentemente reaccionan a e-
ventos. Se corresponden con los objetos reales del mundo que nos rodea, o con ob-
jetos internos del sistema(del programa). En realidad, un objeto es una instancia
de una clase, por lo que se pueden interncambiar los terminos objeto o instancia.
Un ejemplo de objeto podria ser un automovil, en el que tendriamos atributos como
la marca, el numero de puertas o el color y metodos como arrancar y parar. O bien
cualquier otra combinacion de atributos y metodos segun lo que fuera relevante pa-
ra nuestro programa.

Un OBJETO consta de:
    
    > Tiempo de vida: la duracion de un objeto en un programa siempre esta limita-
                    da en el tiempo. La mayoria de los objetos solo existen duran-
                    te una parte de la ejecucion del programa. Los objetos son cre-
                    ados mediante un mecanismo de instanciacion, y cuando dejan de
                    existir se dice que son destruidos.
    
    > Estado: todo objeto posee un estado, definido por sus atributos, con el se de-
            finen las propiedades del objeto, y el estado en el que se encuentra en
            un momento determinado de su existencia.
    
    > Comportamiento: todo objeto ha de presentar una interfaz, definida por sus me-
                    todos, para que el resto de objetos que componen los programas
                    puedan interactuar con el.
    
    > Identidad: propiedad del objeto que lo distingue de los de demas.

El equivalente de un objeto en el paradigma estructurado seria una variable. Asi mis-
mo la instanciacion de objetos equivaldria a la declaracion de variables, y el tiem-
po de vida de un objeto al ambito(zona del programa donde es usada) de una variable.
'''

# Definir la clase Persona con sus metodos y atributos
class Persona:

    def __init__(self,nombre,edad,genero,estatura,peso):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.estatura = estatura
        self.peso = peso

    def hablar(self):
        print(f"Hola soy {self.nombre}")

    def correr(self):
        print(f"{self.nombre} está corriendo")

    def caminar(self):
        print(f"{self.nombre} está caminando")

'''
El metodo __init__, se ejecuta justo despues de crear un nuevo objeto a partir de la
clase, proceso que se conoce con el nombre de instanciacion.

El metodo __init__ sirve, para realizar cualquier proceso de inicializacion que sea
necesario como puede ser la asignacion de valores a atributos, calculos, llamadas a
otras funciones o procedimientos.

Como vemos, el primer parametro de __init__ y del resto de metodos de la clase es
siempre SELF que sirve para referirse al objeto actual.
Este mecanimos es necesario para poder acceder a los atributos y metodos del objeto
diferenciando, por ejemplo, una variable local mi_var de un atributo del objeto
self.mi_var

Si volvemos al metodo __init__ de nuestra clase Persona veremos como se utiliza self
para asignar al atributo nombe del objeto(self.nombre) el valor que el programador
especifica para el parametro nombre. El parametro nombre se destruye al final de la
funcion, mientras que el atributo nombre se conserva mientras el objeto viva.

Para crear un objeto se escribira el nombre de la clase seguido de cualquier parame-
tro que sea necesario entre parentesis. Estos parametros son los que se pasarn al me-
todo __init__, que como deciamos es el metodo que se llama al instanciar la clase.
'''

persona1 = Persona('Damian',30,'Masculino',1.73,87)
persona2 = Persona('Teresita',34,'Femenino',1.51,75)

'''
En el ejemplo, podemos ver que aunque la definicion de la funcion indica claramente
que precisa de 6 parametros, a la hora de crear un objeto de esta clase pasaremos so-
lo 5 parametros. Esto es asi porque Python para el primer argumento automaticamente.

Ahora que ya hemos creado nuetros objetos, podemos acceder a los atributos y metodos
mediante la sintaxis OBJETO.ATRIBUTO y OBJETO.METODO()
'''

# ATRIBUTOS
print(persona1.nombre)
# Damian
print(persona1.edad)
# 30
print(persona1.genero)
# Marculino
print(persona1.estatura)
# 1.73
print(persona1.peso)
# 87

# METODOS
persona1.hablar()
persona1.correr()
persona1.caminar()