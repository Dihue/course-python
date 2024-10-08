class CuentaBancaria:
    def __init__(self,saldo):
        # Atributo privado
        self.__saldo = saldo
    
    def depositar(self,monto):
        self.__saldo += monto
    
    # def mostrar_saldo(self):
    #    return f"Saldo actual: ${self.saldo}"

    def get_saldo(self):
        return self.__saldo


cuenta = CuentaBancaria(10000)

print(f"Tengo: $ {cuenta.saldo}")
cuenta.depositar(500)
print(cuenta.mostrar_saldo())

# Cambia el valor poque es público
cuenta.saldo = 0
print(cuenta.mostrar_saldo())