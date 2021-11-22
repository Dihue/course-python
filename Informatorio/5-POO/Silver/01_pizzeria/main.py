
class Menu:
    def saludo(self):
        return "Hola mundo"


class Main:
    menu = Menu.saludo()
    print(menu)


objeto = Main()

print(objeto)