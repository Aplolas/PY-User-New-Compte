from compte_banque import CuentaBancaria

#!CREACION CLASE USUARIO.

class Usuario:
    def __init__(self , username, mail, account):
        self.name = username
        self.mail = mail
        self.all_comptes = []
        self.cuenta = CuentaBancaria(account, interes=0.5, balance=0)
        self.all_comptes.append(self.cuenta)

#!AGREGAMOS EL METODO DEPOSITO.

    def realizar_deposito(self, monto):
        self.cuenta.deposito(monto)
        return self
    
    def abrir_nueva_cuenta(self, account):
        nueva_cuenta = CuentaBancaria(account, interes=0.5, balance=0)
        self.all_comptes.append(account, nueva_cuenta=nueva_cuenta)
        return self
    
    def deposito_en_cuenta(self, account, amount):
        for cuenta in self.all_comptes:
            if cuenta.account == account:
                cuenta.deposito(amount)
        return self

    def retiro_dinero(self,amount):
        self.cuenta.retiro(amount)
        return self

    def mostrar_balance(self):
        self.cuenta.mostrar_cuenta()
        return self

    def mostrar_cuenta_usuario(self):
        for cuenta in self.all_comptes:
            print(f" La cuenta #{cuenta.account} del cliente {self.name} tiene un balance de {cuenta.balance}")
        return self

    def  transferencia_dinero(self, otro_user, amount):
        self.cuenta.retiro(amount)
        otro_user.cuenta.deposito(amount)
        return self

Andrea = Usuario('Andrea Perez Lolas', 'a.perez@mail.com', 27543601)  
Zoe = Usuario('Zoe Le Baux Perez Lolas', 'zoe@mail.com', 27543602)
Antoine = Usuario ('Antoine Le Baux', 'a.lebaux@mail.com',27543603)

Andrea.realizar_deposito(100).deposito_en_cuenta(27543601,200).realizar_deposito(500).retiro_dinero(20).transferencia_dinero(Zoe,100).mostrar_cuenta_usuario()
Zoe.deposito_en_cuenta(27543602,300).deposito_en_cuenta(27543602,300).retiro_dinero(100).retiro_dinero(50).mostrar_cuenta_usuario()
Antoine.deposito_en_cuenta(27543603,800).retiro_dinero(100).retiro_dinero(100).retiro_dinero(200).transferencia_dinero(Zoe,50).mostrar_cuenta_usuario()