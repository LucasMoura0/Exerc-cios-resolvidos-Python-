# Função para calcular a bonificação com base na quantidade de inscritos e na presença de conteúdo premium
def calcular_bonificacao(inscritos, monetizacao, conteudo_premium):
    valor_fixo = X if conteudo_premium else Y
    bonificacao = monetizacao + (inscritos // 1000) * valor_fixo
    return bonificacao

# Lê o valor X e Y da ImpacTube
X = float(input("Informe o valor de bonificação para canais com conteúdo premium (X): "))
Y = float(input("Informe o valor de bonificação para canais sem conteúdo premium (Y): "))

# Inicializa a lista de canais
canais = []

# Solicita os dados de cada canal e os armazena na lista
n = int(input("Informe o número de canais: "))
for i in range(n):
    nome_canal = input(f"Nome do canal {i + 1}: ")
    inscritos = int(input(f"Inscritos do canal {i + 1}: "))
    monetizacao = float(input(f"Monetização do último mês do canal {i + 1}: "))
    conteudo_premium = input(f"O canal {nome_canal} produz conteúdo premium? (S/N): ").upper() == 'S'
    canais.append((nome_canal, inscritos, monetizacao, conteudo_premium))

# Calcula e exibe a bonificação para cada canal
print("\nBonificações:")
for canal in canais:
    nome_canal, inscritos, monetizacao, conteudo_premium = canal
    bonificacao = calcular_bonificacao(inscritos, monetizacao, conteudo_premium)
    print(f"{nome_canal}: R$ {bonificacao:.2f}")
