# acumulação de valores em variáveis através do while



nome = 'Alberto Augusto'

indice = 0
nome_novo = ''
while indice < len(nome):
    letra = nome[indice]
    nome_novo += f'{letra} *'
    indice += 1
print('*', nome_novo)