salário = float(input('Digite o salário do funcionário: '))
aumento = int(input('Digite o valor do aumento: '))

novo_salário = salário + (salário * (aumento / 100))
valor_dia = novo_salário / 30

print(f'O novo salário do funcionário será de R${novo_salário:.2f}')
print(f'E o seu valor por dia trabalhado é de R${valor_dia}')
