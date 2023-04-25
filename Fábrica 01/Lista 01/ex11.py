valor_produto = float(input('Qual o valor do produto? '))
desconto = int(input('Qual o valor do desconto em porcentagem? '))

valor_final = valor_produto - (valor_produto * (desconto / 100))

print(f'O produto que vale R${valor_produto} com um desconto de {desconto}% passa a valer R${valor_final}')
