#exemplo de programação orientada a objetos

class ContaCorrente:
    def __init__(self, numero):
        self.saldo = 0
        self.numero = numero

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        print("Novo saldo: ", self.saldo)
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
        else:
            raise ValueError("Saldo insuficiente")
        print("Novo saldo: ", self.saldo)
        return self.saldo

class Banco:
    def __init__(self):
        self.numero_conta = 1
        self.contas = list()

    
    def obter_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None


    def criar_conta(self):
        nova_conta = ContaCorrente(self.numero_conta)
        self.numero_conta += 1 
        self.contas.append(nova_conta)

    def transferir(self, origem, destino, valor):
        conta_origem = self.obter_conta(origem)
        conta_destino = self.obter_conta(destino)
        
        conta_origem.sacar(valor)
        conta_destino.depositar(valor)

        print("Transferencia realizada")
        print("Novo saldo origem", conta_origem.saldo)
        print("Novo saldo destino", conta_destino.saldo)

    def depositar(self, numero_conta, valor):
        conta = self.obter_conta(numero_conta)
        conta.depositar(valor)

    def sacar(self, numero_conta, valor):
        conta = self.obter_conta(numero_conta)
        conta.sacar(valor)

# Meu programa

banco = Banco()
banco.criar_conta()
banco.criar_conta()
banco.depositar(1, 30)
banco.depositar(2, 50)
banco.transferir(1, 2, 20)