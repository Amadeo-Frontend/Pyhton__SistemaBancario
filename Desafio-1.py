class SistemaBancario:
    def __init__(self):
        self._saldo = 0
        self._depositos = []
        self._saques = []
        self._saques_diarios = 0

    def depositar(self, valor):
        if valor <= 0:
            print("O valor do depósito deve ser maior que zero.")
            return
        self._saldo += valor
        self._depositos.append(valor)

    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser maior que zero.")
            return
        if self._saques_diarios >= 3 or valor > 500 or valor > self._saldo:
            print("Não será possível sacar o dinheiro por falta de saldo ou exceder o limite diário de R$500,00.")
            return
        self._saldo -= valor
        self._saques.append(valor)
        self._saques_diarios += 1

    def extrato(self):
        if not self._depositos and not self._saques:
            return "Não foram realizadas movimentações."

        extrato = "Extrato:\n"
        extrato += "Depósitos:\n"
        for deposito in self._depositos:
            extrato += f" - Depósito: R$ {deposito:.2f}\n"
        extrato += "Saques:\n"
        for saque in self._saques:
            extrato += f" - Saque: R$ {saque:.2f}\n"
        extrato += f"Saldo atual: R$ {self._saldo:.2f}"
        return extrato


# Exemplo de uso do sistema bancário
banco = SistemaBancario()
banco.depositar(3000)
banco.sacar(200)
banco.sacar(700)
banco.depositar(500)
print(banco.extrato())