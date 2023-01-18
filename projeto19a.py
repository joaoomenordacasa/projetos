salario = float(input('digite o seu salário: R$'))
if salario <=1250:
    novo = salario + (salario  * 15 / 100)
else:
    novo = salario + (salario *10 / 100)
    print('quem ganhava R${:.2f} passou a ganhar R${:.2f}'.format(salario, novo))