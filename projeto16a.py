distancia = float(input('digite a distancia da viagem!'))
print('você esta prestes a começar uma viagem de até {} Km'.format(distancia))
if distancia <= 200:
    preço = distancia  * 0.50
else:
    preço = distancia * 0.45
print('e o preço da sua passagem será de R${:.2f}'.format(preço))
    