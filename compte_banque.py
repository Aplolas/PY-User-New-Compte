
#!Creacion de nueva clase CuentaBancaria.

class CuentaBancaria:
    def __init__(self,account,interes,balance):
        self.account= account
        self.interes = interes
        self.balance = balance


    #!METODO DE DEPOSITO

    def deposito(self, amount):
        self.balance +=amount
        return self

    #!METODO DE RETIRO

    def retiro(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Fondos insuficientes: Por favor, cargar $5 pesos")
            self.balance -= 5
        return self


    #!METODO PARA MOSTRAR INFO DE LA CUENTA.

    def mostrar_cuenta(self):
        print(f"Balance: {self.balance}")
        return self


    #!METODO PARA GENERAR INTERESES.

    def generar_interes(self):
        if self.balance > 0 :
            self.balance += (self.balance * self.interes)
        return self