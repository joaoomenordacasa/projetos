salário=float(input('Digite o seu salário! R$'))
novo= salário + ( salário * 15 / 100)
print('o salário do funcionário é R${:.2f}, com 15% de aumento, será R${:.2f}!'.format(salário, novo))