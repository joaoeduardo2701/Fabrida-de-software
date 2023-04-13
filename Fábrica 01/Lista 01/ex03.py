n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print('Selecione uma das opções abaixo: ')
print('[ 1 ] Somar')
print('[ 2 ] Subtrair')
print('[ 3 ] Multiplicar')
print('[ 4 ] Dividir')

resposta = int(input('Qual operação você deseja utilizar? '))

if resposta == 1:
    resposta = n1 + n2
    print(f'A soma entre {n1} e {n2} é igual a {resposta}')
elif resposta == 2:
    resposta = n1 - n2
    print(f'A subtração entre {n1} e {n2} é igual a {resposta}')
elif resposta == 3:
    resposta = n1 * n2
    print(f'A multiplicação entre {n1} e {n2} é igual a {resposta}')
elif resposta == 4:
    resposta = n1 / n2
    print(f'A divisão entre {n1} e {n2} é igual a {resposta}')
else:
    print('Por favor insira um valor válido')
