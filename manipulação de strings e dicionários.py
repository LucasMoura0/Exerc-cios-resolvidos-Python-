# Criando um dicionário vazio
dicionario = {}

# Adicionando itens ao dicionário
dicionario['nome'] = 'Maria'
dicionario['idade'] = 25
dicionario['cidade'] = 'São Paulo'

# Imprimindo o dicionário
print("Dicionário inicial:", dicionario)

# Removendo um item do dicionário
if 'idade' in dicionario:
    del dicionario['idade']

# Imprimindo o dicionário após a remoção
print("Dicionário após remover 'idade':", dicionario)

# Iterando sobre as chaves e valores do dicionário
print("Chaves e valores do dicionário:")
for chave, valor in dicionario.items():
    print(f"Chave: {chave}, Valor: {valor}")

# Manipulação de strings
frase = "Python é uma linguagem poderosa e versátil"

# Dividindo a string em uma lista de palavras
lista_palavras = frase.split()

# Imprimindo a lista de palavras
print("\nLista de palavras:", lista_palavras)

# Juntando as palavras da lista em uma string novamente
nova_frase = ' '.join(lista_palavras)
print("Nova frase:", nova_frase)

# Verificando a ocorrência de uma palavra na frase
palavra_chave = 'linguagem'
if palavra_chave in nova_frase:
    print(f"\nA palavra '{palavra_chave}' está na frase.")
else:
    print(f"\nA palavra '{palavra_chave}' não está na frase.")
