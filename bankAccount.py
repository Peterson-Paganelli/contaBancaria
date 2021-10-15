from client import client

class bankAccount(client):
    __agencia = None;
    __saldo = 0.0;
    __limite = 0.0;
    def __init__(self):
        super().__init__()
        self.__agencia = 1;
        self.__saldo = 0.0;
        self.__limite = 0.0;
        #super().get_name("Peter")        
        #super().get_cpf(11111)
        #super().get_rg(111111)

        
    def get_agencia(self):
        return self.__agencia;


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
        print("Saldo: {}\nTitular: {}".format(self.__saldo, self.__name));

 
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


    def __del__(self):
        self.__agencia = None;
        self.__saldo = 0.0;
        self.__limite = 0.0;
        print("Conta excluída")        



conta1 = bankAccount(1, 500.00, 1000.00);
conta2 = bankAccount(1, 500.00, 1000.00);

print("Agência:", conta1.get_agencia(),"Saldo:", conta1.get_saldo(),"Limite:", conta1.get_limite());
print("Agência:", conta2.get_agencia(),"Saldo:", conta2.get_saldo(),"Limite:", conta2.get_limite());

valor = 200.00;


conta1.sacar(valor);
print("\nTeste1:", conta1.get_saldo());

conta1.extrato();

conta1.depositar(valor);
print("\nTeste3:", conta1.get_saldo());

conta1.transferir(valor, conta2);
print("\nTeste4:", conta1.get_saldo());
print("Teste4:", conta2.get_saldo());

