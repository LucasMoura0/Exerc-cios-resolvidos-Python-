itens = []
separador = '-' * 20
entrada = ""
itens_noivo = []
itens_noiva = []
itens_ambos = []
item_noivo = ""
item_noiva = ""

itens_apenas_um = []
nova_lista = []

while entrada != 'ACABOU':
    linha = str(input())
    entrada = linha
    if entrada == 'ACABOU':
        break
    itens.append(linha)

for item in itens:
    if ';noivo' in item:
        item_noivo = item.replace(';noivo', '')
        itens_noivo.append(item_noivo)
    elif ';noiva' in item:
        item_noiva = item.replace(';noiva', '')
        itens_noiva.append(item_noiva)

nova_lista.extend(itens_noiva)
nova_lista.extend(itens_noivo)

for item_noiva in itens_noiva:
    if item_noiva in itens_noivo:
        itens_ambos.append(item_noiva)

for item_noivo in nova_lista:
    if item_noivo not in itens_ambos:
        itens_apenas_um.append(item_noivo)

itens_noiva = [item for item in itens_noiva if item not in itens_ambos]
itens_noivo = [item for item in itens_noivo if item not in itens_ambos]

itens_unicos = list(set(nova_lista))
itens_ordenados = sorted(itens_unicos)

print(f'{separador}')
print('LISTA FINAL')
print(f'{separador}')
for item in itens_ordenados:
    print(f'{item}')
print('')

itens_noiva_unicos = list(set(itens_noiva))
itens_ordenados_noiva = sorted(itens_noiva_unicos)

print(f'{separador}')
print('APENAS NOIVA')
print(f'{separador}')
for item_noiva in itens_ordenados_noiva:
    print(f'{item_noiva}')
print('')

itens_noivo_unicos = list(set(itens_noivo))
itens_ordenados_noivo = sorted(itens_noivo_unicos)

print(f'{separador}')
print('APENAS NOIVO')
print(f'{separador}')
for item_noivo in itens_ordenados_noivo:
    print(f'{item_noivo}')
print('')

itens_ordenados_ambos = sorted(itens_ambos)

print(f'{separador}')
print('POR AMBOS')
print(f'{separador}')
for item_ambos in itens_ordenados_ambos:
    print(f'{item_ambos}')
print('')

itens_apenas_um_unicos = list(set(itens_apenas_um))
itens_ordenados_apenas_um = sorted(itens_apenas_um_unicos)

print(f'{separador}')
print('POR APENAS UM DELES')
print(f'{separador}')
for item_apenas_um in itens_ordenados_apenas_um:
    print(f'{item_apenas_um}')
e
