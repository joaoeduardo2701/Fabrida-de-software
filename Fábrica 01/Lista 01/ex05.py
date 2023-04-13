lado1 = float(input('Digite o valor do primeiro lado do triângulo:'))
lado2 = float(input('Digite o valor do segundo lado do triângulo: '))
lado3 = float(input('Digite o valor do terceiro lado do triângulo: '))

if lado1 + lado2 < lado3 or lado1 + lado3 < lado2 or lado2 + lado3 < lado1:
    print('Esses segmentos de reta não formam um triângulo!')
elif lado1 == lado2 == lado3:
    print('Triângulo equilátero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Triângulo isóceles')
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print('Triângulo escaleno')
