from abc import ABC, abstractmethod

# Classe abstrata ContaBancaria
# Define o esqueleto de uma conta bancária, que outras classes (ContaCorrente e ContaPoupanca) irão herdar
class ContaBancaria(ABC):
    def __init__(self, num_conta, titular, saldo=0.0):
        # Inicializa os atributos básicos da conta bancária
        self.num_conta = num_conta
        self.titular = titular
        self.saldo = saldo

    # Métodos abstratos: as classes filhas precisam implementar
    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    # Método para visualizar o saldo da conta
    def ver_saldo(self):
        print(f'Conta: {self.num_conta} | Titular: {self.titular} | Saldo: R${self.saldo:.2f}')

# Classe ContaCorrente herda de ContaBancaria
class ContaCorrente(ContaBancaria):
    def __init__(self, num_conta, titular, saldo=0.0, cheque_especial=-1000.0):
        # Chama o construtor da superclasse (ContaBancaria)
        super().__init__(num_conta, titular, saldo)
        # Define o limite do cheque especial
        self.cheque_especial = cheque_especial

    # Implementação do método sacar
    def sacar(self, valor):
        if self.saldo - valor < self.cheque_especial:
            print(f'Saque de R${valor:.2f} negado! Limite do cheque especial atingido.')
            return False
        self.saldo -= valor
        print(f'Saque de R${valor:.2f} realizado com sucesso!')
        return True

    # Implementação do método depositar
    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:.2f} realizado com sucesso!')
        return True

# Classe ContaPoupanca herda de ContaBancaria
class ContaPoupanca(ContaBancaria):
    def __init__(self, num_conta, titular, saldo=0.0, taxa_juros=0.005):
        # Chama o construtor da superclasse (ContaBancaria)
        super().__init__(num_conta, titular, saldo)
        # Define a taxa de juros para a conta poupança
        self.taxa_juros = taxa_juros

    # Implementação do método sacar
    def sacar(self, valor):
        if self.saldo - valor < 0:
            print(f'Saque de R${valor:.2f} negado! Saldo insuficiente.')
            return False
        self.saldo -= valor
        print(f'Saque de R${valor:.2f} realizado com sucesso!')
        return True

    # Implementação do método depositar
    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:.2f} realizado com sucesso!')
        return True

    # Método para calcular os juros e adicionar ao saldo
    def calcular_juros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros
        print(f'Juros de R${juros:.2f} aplicados. Saldo atual: R${self.saldo:.2f}')
        return self.saldo

# Função para realizar operações na conta (sacar, depositar, ver saldo)
def operacoes_conta(conta):
    while True:
        print('\n1 - Sacar\n2 - Depositar\n3 - Ver Saldo\n4 - Calcular Juros\n0 - Sair')  # Opção 4 adicionada para calcular juros
        try:
            operacao = int(input('Escolha uma operação: '))
        except ValueError:
            print('Opção inválida! Por favor, insira um número válido.')
            continue

        if operacao == 1:
            try:
                valor = float(input('Informe o valor do saque: R$'))
                conta.sacar(valor)
            except ValueError:
                print('Valor inválido!')
        elif operacao == 2:
            try:
                valor = float(input('Informe o valor do depósito: R$'))
                conta.depositar(valor)
            except ValueError:
                print('Valor inválido!')
        elif operacao == 3:
            conta.ver_saldo()
        elif operacao == 4:  # Chama o método calcular_juros para contas poupança
            if isinstance(conta, ContaPoupanca):
                conta.calcular_juros()
            else:
                print('Opção não disponível para Conta Corrente!')
        elif operacao == 0:
            print('Encerrando...')
            break
        else:
            print('Opção inválida!')

# Função principal
def main():
    while True:
        print('\n1 - Conta Poupança\n2 - Conta Corrente\n0 - Sair')
        try:
            opcao = int(input('Escolha o tipo de conta: '))
        except ValueError:
            print('Opção inválida! Por favor, insira um número válido.')
            continue

        if opcao == 1:
            try:
                saldo = float(input('Informe o saldo inicial: R$'))
                n_conta = int(input('Informe o número da conta: '))
                nome = input('Informe o nome do titular: ').capitalize()
                conta_usuario = ContaPoupanca(n_conta, nome, saldo)
                operacoes_conta(conta_usuario)
            except ValueError:
                print('Dados inválidos! Verifique as entradas e tente novamente.')
        elif opcao == 2:
            try:
                saldo = float(input('Informe o saldo inicial: R$'))
                n_conta = int(input('Informe o número da conta: '))
                nome = input('Informe o nome do titular: ').capitalize()
                conta_usuario = ContaCorrente(n_conta, nome, saldo)
                operacoes_conta(conta_usuario)
            except ValueError:
                print('Dados inválidos! Verifique as entradas e tente novamente.')
        elif opcao == 0:
            print('Saindo...')
            break
        else:
            print('Opção inválida!')

if __name__ == '__main__':
    main()
