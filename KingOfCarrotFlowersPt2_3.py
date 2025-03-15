nome = input('Qual o seu nome? ')
altura = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso? '))
imc = peso / altura ** 2

print(f'{nome} seu IMC é {imc:.2f}')