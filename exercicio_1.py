entrada = input('Digite um número inteiro: ')

if entrada.isdigit():
    entrada_int= int(entrada)
    par = entrada_int %2 == 0
    if par:
        print(f'O número {entrada_int} é par')
    else:
        print(f'O número {entrada_int} é impar')

else:
    print('O número digitado não é inteiro.')



