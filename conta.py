class ContaBancaria():

    def __init__(self, agencia, titular, saldo, limite):
        self.__agencia = agencia;
        self.__titular = titular;
        self.__saldo = saldo;
        self.__limite = limite;


    def get_agencia(self):
        return self.__agencia;


    def get_titular(self):
        return self.__titular;


    def get_saldo(self):
        return self.__saldo;


    def set_saldo(self, saldo):
        self.__saldo = saldo;


    def get_limite(self):
        return self.__limite;


    def set_limite(self, limite):
        self.__limite = limite;



    def extrato(self):
        print("\nExtrato Bancário:");
        print("Saldo: {}\nTitular: {}".format(self.__saldo, self.__titular));

 
    def sacar(self, valor):
        if(self.__saldo >= valor):
            self.__saldo -= valor;
            return valor;


    def depositar(self, valor):
        if(valor <= 0):  
            return;
        else:
            self.__saldo += valor;


    def transferir(self, valor, conta):
        valorSacado = self.sacar(valor);
        conta.depositar(valorSacado);      



conta1 = ContaBancaria(1, "Peter", 500.00, 1000.00);
conta2 = ContaBancaria(1, "Peterson", 500.00, 1000.00);

print("Agência:", conta1.get_agencia(),"Titular:", conta1.get_titular(),"Saldo:", conta1.get_saldo(),"Limite:", conta1.get_limite());
print("Agência:", conta2.get_agencia(),"Titular:", conta2.get_titular(),"Saldo:", conta2.get_saldo(),"Limite:", conta2.get_limite());

valor = 200.00;


conta1.sacar(valor);
print("\nTeste1:", conta1.get_saldo());

conta1.extrato();

conta1.depositar(valor);
print("\nTeste3:", conta1.get_saldo());

conta1.transferir(valor, conta2);
print("\nTeste4:", conta1.get_saldo());
print("Teste4:", conta2.get_saldo());
