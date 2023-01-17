preço=float(input('digite o preço do produto! R$'))
novo= preço - (preço * 5 / 100)
print('o preço do produto {}R$ com desconto de 5% de desconto será R$ {:.2f}'.format(preço, novo))