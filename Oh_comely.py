nome = input('Qual seu nome? ')
altura = float(input('Qual sua altura(em metros)? '))
peso = float(input('Qual seu peso?'))
imc = peso / altura ** 2

linha_1 = f'{nome} tem  {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)