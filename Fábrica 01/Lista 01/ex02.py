nota1 = float(input('Nota 1:'))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print('Você foi APROVADO!')
else:
    print('Você foi REPROVADO!')

print(f'A média das notas é de {media}')
