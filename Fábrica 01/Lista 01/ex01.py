altura = float(input('Qual a sua altura: '))
sexo = str(input('Qual o seu sexo (M/F)? '))

if sexo.upper() == 'M':
    peso_ideal = (altura * 72.7) - 58 
elif sexo.upper() == 'F':
    peso_ideal = (altura * 62.1) - 44.7


print(f'O seu peso ideal é de {peso_ideal:.1f}kg')
