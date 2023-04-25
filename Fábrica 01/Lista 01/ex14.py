dias_alugados = int(input('Quantidade de dias alugados: '))
km_rodados = float(input('Quantidade de km rodados: '))

valor_dias_alugados = dias_alugados * 30
valor_km_rodados = km_rodados * 0.8
valor_total = valor_dias_alugados + valor_km_rodados

print(f'O valor por dia alugados foi de R${valor_dias_alugados} e o valor de km rodados foi de R${valor_km_rodados}, resultando em um total de R${valor_total}')
