print('Escolha uma das opções abaixo: ')
print('[ 1 ] Soma de 2 valores')
print('[ 2 ] Diferença de 2 valores')
print('[ 3 ] Produto de 2 valores')
print('[ 4 ] Divisão de 2 valores')

operação = int(input('-> '))

n1 = int(input('Qual valor deseja realizar a operação: '))
n2 = int(input('Qual o outro valor que deseja realizar a operação: '))

if operação == 1:
    resultado = n1 + n2
    print(f'A soma entre {n1} e {n2} é igual a {resultado}')
elif operação == 2:
    resultado = n1 - n2
    print(f'A diferença entre {n1} e {n2} é igual a {resultado}')
elif operação == 3:
    resultado = n1 * n2
    print(f'O produto entre {n1} e {n2} é igual a {resultado}')
elif operação == 4:
    resultado = n1 / n2
    print(f'A divisão entre {n1} e {n2} é igual a {resultado}')
else:
    print('Por favor insira um valor válido')
