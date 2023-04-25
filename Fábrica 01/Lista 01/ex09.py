real = float(input('Digite um valor em reais: '))

dolar = real / 5.07

euro = real / 5.56

print(f'R${real:.2f} equivale a US${dolar:.2f} e {euro:.2f}€')