entrada = input('Digite as horas em números inteiros: ')

if entrada.isdigit():
    horas= int(entrada)
    saudacoes_dia = horas >= 0 and horas <= 11
    saudacoes_tarde= horas  >= 12 and horas <=17
    saudacoes_noite = horas >= 18 and horas <=23


    if saudacoes_dia:
        saudacoes_texto = 'bom dia.'
    if saudacoes_tarde:
        saudacoes_texto = 'boa tarde.'
    if saudacoes_noite:
        saudacoes_texto = 'boa noite'
        

else:
    print('Isso é uma hora inválida ou um número não inteiro.')

print(saudacoes_texto)


