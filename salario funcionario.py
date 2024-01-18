class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumenta_salario(self, valor):
        self.salario += valor

    def reduz_salario(self, valor):
        if valor >= self.salario:
            self.salario = 0
        else:
            self.salario -= valor

def encontrar_funcionario(funcionarios, nome):
    for funcionario in funcionarios:
        if funcionario.nome == nome:
            return funcionario
    return None

N = int(input())
funcionarios = []

for _ in range(N):
    nome, salario = input().split()
    salario = float(salario)
    funcionario = Funcionario(nome, salario)
    funcionarios.append(funcionario)

while True:
    operacao = input().split()
    if operacao[0] == 'FIM':
        break

    nome_funcionario = operacao[2]
    valor = float(operacao[1])

    funcionario = encontrar_funcionario(funcionarios, nome_funcionario)
    if funcionario:
        if operacao[0] == 'aumenta':
            funcionario.aumenta_salario(valor)
        elif operacao[0] == 'reduz':
            funcionario.reduz_salario(valor)

for funcionario in funcionarios:
    print(f"Nome: {funcionario.nome}")
    print(f"Salário: R$ {funcionario.salario:.2f}")
    print('-' * 20)
